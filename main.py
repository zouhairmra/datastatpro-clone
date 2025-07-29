# main.py

import streamlit as st

st.set_page_config(
    page_title="📚 منصة الاقتصاد التفاعلية",
    layout="centered",
    page_icon="📊"
)

# Arabic RTL styling
st.markdown(
    """
    <style>
        html, body, [class*="css"] {
            direction: rtl;
            text-align: right;
            font-family: 'Amiri', 'Cairo', sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📚 منصة الاقتصاد التفاعلية")

st.markdown("""
مرحبًا بك في منصة تعليمية تفاعلية مصممة خصيصًا لطلبة الاقتصاد 🎓  
اختر من القائمة الجانبية:

- 🧠 لعبة نظرية الألعاب
- ⚖️ توازن السوق بالرسم التفاعلي
- قريبًا: نماذج اقتصادية، اختبارات تفاعلية، موارد تعليمية 📘
""")

st.info("اختر الصفحة من القائمة الجانبية ⬅️")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray;'>جميع الحقوق محفوظة © 2025 | datastatpro</div>",
    unsafe_allow_html=True
)
