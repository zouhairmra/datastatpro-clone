# pages/quiz_market_equilibrium.py

import streamlit as st

st.set_page_config(page_title="📝 اختبر نفسك: توازن السوق", layout="centered")

st.title("📝 اختبر نفسك: توازن السوق")

question = st.radio("إذا كان السعر أقل من سعر التوازن، فإن السوق سيعاني من:", 
                    ["فائض في العرض", "نقص في العرض", "توازن", "ارتفاع الإنتاج"])

if st.button("تحقق من الإجابة"):
    if question == "نقص في العرض":
        st.success("✔️ إجابة صحيحة! يحدث نقص عندما يكون السعر منخفضًا.")
    else:
        st.error("❌ إجابة غير صحيحة. حاول مرة أخرى.")
