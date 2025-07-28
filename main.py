import streamlit as st

st.set_page_config(page_title="لعبة السجينين الذكية", layout="centered")
st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)

st.title("🎯 لعبة السجينين: جولات متعددة واستراتيجية ذكية")
st.write("العب ضد الكمبيوتر الذي يتبع استراتيجية Tit for Tat!")

# إعداد عدد الجولات
num_rounds = st.slider("🔢 عدد الجولات", min_value=1, max_value=10, value=5)

# خيارات اللعب
choices = ["🤝 التعاون", "❌ الخيانة"]

# تحميل الحالة أو تهيئتها
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.student_moves = []
    st.session_state.computer_moves = []
    st.session_state.results = []

# عرض الجولة الحالية
st.subheader(f"الجولة رقم {st.session_state.round} من {num_rounds}")
student_move = st.radio("📌 اختر حركتك:", choices, key=f"move_{st.session_state.round}")

if st.button("🔁 تأكيد الجولة"):

    # تحديد حركة الكمبيوتر (Tit for Tat)
    if st.session_state.round == 1:
        computer_move = "🤝 التعاون"
    else:
        computer_move = st.session_state.student_moves[-1]  # يقلّد الطالب

    # حساب النتائج
    payoff_matrix = {
        ("🤝 التعاون", "🤝 التعاون"): (3, 3),
        ("🤝 التعاون", "❌ الخيانة"): (0, 5),
        ("❌ الخيانة", "🤝 التعاون"): (5, 0),
        ("❌ الخيانة", "❌ الخيانة"): (1, 1)
    }
    student_score, computer_score = payoff_matrix[(student_move, computer_move)]

    # حفظ النتائج
    st.session_state.student_moves.append(student_move)
    st.session_state.computer_moves.append(computer_move)
    st.session_state.results.append((student_score, computer_score))

    st.success(f"🎮 الجولة {st.session_state.round} مكتملة!")
    st.write(f"🧑‍🎓 أنت: {student_move} | 💻 الكمبيوتر: {computer_move}")
    st.write(f"✅ النتيجة: أنت {student_score} - الكمبيوتر {computer_score}")

    st.session_state.round += 1

# عند انتهاء الجولات
if st.session_state.round > num_rounds:
    total_student = sum(x[0] for x in st.session_state.results)
    total_computer = sum(x[1] for x in st.session_state.results)

    st.markdown("## 📊 النتائج النهائية")
    st.write(f"🔵 نقاط الطالب: {total_student}")
    st.write(f"🟢 نقاط الكمبيوتر: {total_computer}")

    st.bar_chart({
        "🧑‍🎓 الطالب": [total_student],
        "💻 الكمبيوتر": [total_computer]
    })

    if total_student > total_computer:
        st.success("🎉 مبروك! تفوقت على الكمبيوتر.")
    elif total_student < total_computer:
        st.warning("🤖 الكمبيوتر فاز هذه المرة.")
    else:
        st.info("🔁 تعادل عادل!")

    if st.button("🔄 إعادة اللعب"):
        for key in ["round", "student_moves", "computer_moves", "results"]:
            del st.session_state[key]

st.markdown("</div>", unsafe_allow_html=True)
