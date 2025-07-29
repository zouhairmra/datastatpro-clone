# pages/market_equilibrium.py

import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="⚖️ توازن السوق", layout="centered")

st.title("⚖️ توازن السوق")

# معادلات الطلب والعرض
def quantity_demanded(p): return 100 - 10 * p
def quantity_supplied(p): return 20 + 10 * p

# تهيئة السعر في الجلسة
if 'price' not in st.session_state:
    st.session_state.price = 5

# أزرار التفاعل
col1, col2 = st.columns(2)
with col1:
    if st.button("🔼 رفع السعر"):
        if st.session_state.price < 10:
            st.session_state.price += 1
with col2:
    if st.button("🔽 خفض السعر"):
        if st.session_state.price > 1:
            st.session_state.price -= 1

price = st.session_state.price
qd = quantity_demanded(price)
qs = quantity_supplied(price)

st.subheader(f"📊 السعر الحالي: **{price}**")

# عرض حالة السوق
if qd > qs:
    st.warning(f"📉 هناك **نقص** في السوق: الطلب ({qd}) > العرض ({qs})")
    st.markdown(
        """
        🛒 هذا يؤدي إلى **زيادة السعر** تدريجيًا.  
        مع ارتفاع السعر:
        - ينخفض الطلب
        - يزيد العرض  
        ➡️ حتى نصل إلى **التوازن**.
        """
    )
elif qs > qd:
    st.info(f"📈 هناك **فائض** في السوق: العرض ({qs}) > الطلب ({qd})")
    st.markdown(
        """
        📦 هذا يدفع البائعين إلى **خفض السعر**.  
        مع انخفاض السعر:
        - يزيد الطلب
        - ينخفض العرض  
        ➡️ حتى نصل إلى **التوازن**.
        """
    )
else:
    st.success(f"✅ السعر {price} هو **سعر التوازن**! العرض = الطلب = {qs}")
    st.markdown(
        """
        ⚖️ السوق في حالة توازن.  
        لا يوجد ضغط لرفع أو خفض السعر، والسوق مستقر.
        """
    )

# منحنيي العرض والطلب (السعر على المحور الرأسي)
prices = list(range(1, 11))
demand_quantities = [quantity_demanded(p) for p in prices]
supply_quantities = [quantity_supplied(p) for p in prices]

fig = go.Figure()
fig.add_trace(go.Scatter(x=demand_quantities, y=prices, mode='lines+markers', name='الطلب'))
fig.add_trace(go.Scatter(x=supply_quantities, y=prices, mode='lines+markers', name='العرض'))
fig.add_hline(y=price, line_dash="dot", line_color="gray")

fig.update_layout(
    title="منحنيي العرض والطلب (السعر على المحور الرأسي)",
    xaxis_title="الكمية",
    yaxis_title="السعر"
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")
st.header("🎯 كيف تؤثر العوامل الخارجية على العرض والطلب؟")

factor = st.selectbox(
    "اختر عاملاً للتغير:",
    ["زيادة دخل المستهلكين", "ارتفاع تكلفة الإنتاج", "تحسن التكنولوجيا", "انخفاض عدد الموردين"]
)

# معامل انزياح
shift = 20

if factor == "زيادة دخل المستهلكين":
    st.markdown("💰 **زيادة الدخل** تؤدي إلى زيادة الطلب على السلع العادية.")
    demand_shifted = [q + shift for q in demand_quantities]
    supply_shifted = supply_quantities
    curve_note = "انزياح منحنى الطلب إلى اليمين"
elif factor == "ارتفاع تكلفة الإنتاج":
    st.markdown("🏭 **ارتفاع التكاليف** يجعل المنتجين أقل رغبة في العرض.")
    demand_shifted = demand_quantities
    supply_shifted = [q - shift for q in supply_quantities]
    curve_note = "انزياح منحنى العرض إلى اليسار"
elif factor == "تحسن التكنولوجيا":
    st.markdown("🧠 **تحسن التكنولوجيا** يزيد من كفاءة الإنتاج ويزيد العرض.")
    demand_shifted = demand_quantities
    supply_shifted = [q + shift for q in supply_quantities]
    curve_note = "انزياح منحنى العرض إلى اليمين"
elif factor == "انخفاض عدد الموردين":
    st.markdown("📉 **قلة الموردين** تؤدي إلى انخفاض العرض.")
    demand_shifted = demand_quantities
    supply_shifted = [q - shift for q in supply_quantities]
    curve_note = "انزياح منحنى العرض إلى اليسار"

# رسم الانزياحات
fig2 = go.Figure()

fig2.add_trace(go.Scatter(x=demand_quantities, y=prices, mode='lines', name='الطلب الأصلي', line=dict(dash='dot')))
fig2.add_trace(go.Scatter(x=supply_quantities, y=prices, mode='lines', name='العرض الأصلي', line=dict(dash='dot')))

fig2.add_trace(go.Scatter(x=demand_shifted, y=prices, mode='lines+markers', name='الطلب الجديد'))
fig2.add_trace(go.Scatter(x=supply_shifted, y=prices, mode='lines+markers', name='العرض الجديد'))

fig2.update_layout(
    title=f"📈 {curve_note}",
    xaxis_title="الكمية",
    yaxis_title="السعر",
    yaxis=dict(autorange='reversed')  # السعر من أعلى لأسفل
)

st.plotly_chart(fig2, use_container_width=True)
