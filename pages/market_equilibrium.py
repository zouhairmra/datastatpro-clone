import streamlit as st

def market_equilibrium_page():
    st.set_page_config(page_title="📉 توازن السوق", layout="centered")

    st.markdown("<h2 style='text-align:right; direction:rtl;'>📉 توازن السوق</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:right; direction:rtl; font-size:18px;'>
    في الاقتصاد، يحدث <strong>توازن السوق</strong> عندما يتساوى <strong>الطلب</strong> و<strong>العرض</strong> عند سعر معين، يُعرف بـ <strong>سعر التوازن</strong>. في هذا السعر، لا يوجد فائض أو نقص في السلع.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🧮 ما الذي يحدث في حال وجود خلل في السوق؟")

    st.radio("اختر الحالة لعرض تفسيرها:", ["📈 زيادة (Surplus)", "📉 نقص (Shortage)"], key="equilibrium_case")

    if st.session_state.equilibrium_case == "📈 زيادة (Surplus)":
        st.markdown("""
        <div style='text-align:right; direction:rtl; font-size:18px;'>
        عندما يكون <strong>السعر أعلى</strong> من سعر التوازن، يكون العرض أكبر من الطلب، مما يسبب <strong>زيادة في السوق</strong>. 
        <br><br>
        النتيجة؟ يقوم البائعون <strong>بتخفيض الأسعار</strong> لتحفيز الطلب وتقليل الفائض، حتى يعود السعر إلى التوازن.
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.equilibrium_case == "📉 نقص (Shortage)":
        st.markdown("""
        <div style='text-align:right; direction:rtl; font-size:18px;'>
        عندما يكون <strong>السعر أقل</strong> من سعر التوازن، يكون الطلب أكبر من العرض، مما يسبب <strong>نقصًا في السوق</strong>. 
        <br><br>
        النتيجة؟ يقوم البائعون <strong>برفع الأسعار</strong> بسبب زيادة الطلب وندرة السلعة، إلى أن يعود السعر إلى التوازن.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h4 style='text-align:right; direction:rtl;'>🎓 خلاصة</h4>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:right; direction:rtl; font-size:18px;'>
    السوق دائمًا يميل إلى <strong>التوازن</strong> عبر آلية السعر. فعندما يحدث فائض أو نقص، فإن السعر يتكيف ليعيد السوق إلى نقطة الاستقرار.
    </div>
    """, unsafe_allow_html=True)

