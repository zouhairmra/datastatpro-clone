import streamlit as st

st.set_page_config(page_title="لعبة السجينين - لاعبين", layout="centered")
st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)

st.title("🎯 لعبة السجينين بين طالبين")

# إعداد عدد الجولات
num_rounds = st.slider("🔢 عدد الجولات", min_value=1, max_value=10, value=5)

# خيارات اللعب
choices = ["🤝 التعاون", "❌ الخيانة"]

# تهيئة الحالة
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.player1_moves = []
    st.session_state.player2_moves = []
    st.session_state.results = []

# عرض الجولة
st.subheader(f"🎲 الجولة {st.session_state.round} من {num_rounds}")
player1_move = st.radio("🧑 الطالب 1: اختر حركتك", choices, key=f"p1_{st.session_state.round}")
player2_move = st.radio("👨‍🎓 الطالب 2: اختر حركتك", choices, key=f"p2_{st.session_state.round}")

if st.button("✅ تأكيد الجولة"):

    # حساب النتائج
    payoff_matrix = {
        ("🤝 التعاون", "🤝 التعاون"): (3, 3),
        ("🤝 التعاون", "❌ الخيانة"): (0, 5),
        ("❌ الخيانة", "🤝 التعاون"): (5, 0),
        ("❌ الخيانة", "❌ الخيانة"): (1, 1)
    }
    score1, score2 = payoff_matrix[(player1_move, player2_move)]

    # تخزين النتائج
    st.session_state.player1_moves.append(player1_move)
    st.session_state.player2_moves.append(player2_move)
    st.session_state.results.append((score1, score2))

    st.success(f"✅ الجولة {st.session_state.round} اكتملت!")
    st.write(f"👤 الطالب 1: {player1_move} | 👤 الطالب 2: {player2_move}")
    st.write(f"📊 النتيجة: الطالب 1 = {score1} | الطالب 2 = {score2}")

    st.session_state.round += 1

# عند انتهاء الجولات
if st.session_state.round > num_rounds:
    total1 = sum(r[0] for r in st.session_state.results)
    total2 = sum(r[1] for r in st.session_state.results)

    st.markdown("## 🏁 النتائج النهائية")
    st.write(f"🧑 الطالب 1: {total1} نقطة")
    st.write(f"👨‍🎓 الطالب 2: {total2} نقطة")

    st.bar_chart({
        "👤 الطالب 1": [total1],
        "👤 الطالب 2": [total2]
    })

    if total1 > total2:
        st.success("🎉 الطالب 1 هو الفائز!")
    elif total1 < total2:
        st.success("🎉 الطالب 2 هو الفائز!")
    else:
        st.info("🔁 تعادل بين الطالبين.")

    if st.button("🔄 إعادة اللعب"):
        for key in ["round", "player1_moves", "player2_moves", "results"]:
            del st.session_state[key]

st.markdown("</div>", unsafe_allow_html=True)
