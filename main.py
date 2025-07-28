import streamlit as st
import random

# Arabic UI setup
st.set_page_config(page_title="لعبة السجينين", layout="centered")
st.markdown("<div style='direction: rtl; text-align: right;'>", unsafe_allow_html=True)

st.title("🎲 لعبة السجينين (Prisoner's Dilemma)")

st.write("أنت الآن في مواجهة مع الكمبيوتر. هل ستتعاون أم تخونه؟")

# User choice
student_choice = st.radio("اختر استراتيجيتك:", ["🤝 التعاون", "❌ الخيانة"])

# Simulate computer strategy
strategies = ["🤝 التعاون", "❌ الخيانة"]
computer_choice = random.choice(strategies)

# Payoff matrix
payoffs = {
    ("🤝 التعاون", "🤝 التعاون"): (3, 3),
    ("🤝 التعاون", "❌ الخيانة"): (0, 5),
    ("❌ الخيانة", "🤝 التعاون"): (5, 0),
    ("❌ الخيانة", "❌ الخيانة"): (1, 1)
}

# Show result
if st.button("🎯 العب الآن"):
    payoff = payoffs[(student_choice, computer_choice)]
    
    st.markdown(f"""
    <h4>🧑‍🎓 أنت اخترت: {student_choice}</h4>
    <h4>💻 الكمبيوتر اختار: {computer_choice}</h4>
    <h3>✅ النتيجة: أنت حصلت على {payoff[0]}، والكمبيوتر حصل على {payoff[1]}</h3>
    """, unsafe_allow_html=True)

# Explanation
with st.expander("📘 ما هي لعبة السجينين؟"):
    st.markdown("""
    <p style='direction: rtl; text-align: right;'>
    لعبة السجينين هي أحد أشهر نماذج نظرية الألعاب، وتُستخدم لتحليل قرارات الأفراد عندما تكون هناك منافع متبادلة واحتمال للخيانة. رغم أن التعاون هو الأفضل للطرفين، إلا أن الخيانة قد تُغري البعض لتحقيق مكاسب أكبر.
    </p>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
