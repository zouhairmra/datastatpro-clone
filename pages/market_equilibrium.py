# pages/market_equilibrium.py

import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="⚖️ توازن السوق", layout="centered")

st.title("⚖️ توازن السوق")

# معادلات العرض والطلب (بسيطة)
def quantity_demanded(p): return 100 - 10 * p
def quantity_supplied(p): return 20 + 10 * p

price = st.slider("اختر السعر:", min_value=1, max_value=10, value=5)

qd = quantity_demanded(price)
qs = quantity_supplied(price)

# عرض النتيجة
if qd > qs:
    st.warning(f"📉 هناك **نقص** في السوق: الطلب ({qd}) > العرض ({qs})")
elif qs > qd:
    st.info(f"📈 هناك **فائض** في السوق: العرض ({qs}) > الطلب ({qd})")
else:
    st.success(f"✅ السعر {price} هو **سعر التوازن**! العرض = الطلب = {qs}")

# رسم بياني تفاعلي (الكمية على المحور الأفقي والسعر على المحور الرأسي)
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
