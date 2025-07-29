import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def market_equilibrium_page():
    st.set_page_config(page_title="📉 توازن السوق", layout="centered")

    st.markdown("<h2 style='text-align:right; direction:rtl;'>📉 توازن السوق</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:right; direction:rtl; font-size:18px;'>
    يحدث <strong>توازن السوق</strong> عندما يتساوى <strong>الطلب</strong> و<strong>العرض</strong> عند سعر معين. 
    في هذا السعر، لا يوجد فائض أو نقص في الكمية المتبادلة.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📊 تفاعل: اختر الحالة لعرض منحنيات السوق")

    case = st.radio("اختر الحالة:", ["📈 زيادة (Surplus)", "📉 نقص (Shortage)", "⚖️ توازن"], horizontal=True)

    # إعداد البيانات الأساسية
    price = np.linspace(1, 20, 20)
    demand = 50 - 2 * price      # منحنى الطلب
    supply = 2 * price - 10      # منحنى العرض

    df = pd.DataFrame({
        "السعر": price,
        "الطلب": demand,
        "العرض": supply
    })

    # تعديل حسب الحالة
    if case == "📈 زيادة (Surplus)":
        current_price = 16
        note = "السعر أعلى من التوازن → العرض > الطلب → فائض"
    elif case == "📉 نقص (Shortage)":
        current_price = 6
        note = "السعر أقل من التوازن → الطلب > العرض → نقص"
    else:
        current_price = 10
        note = "السعر عند التوازن → الطلب = العرض"

    demand_at_price = 50 - 2 * current_price
    supply_at_price = 2 * current_price - 10

    fig = px.line(df, x="السعر", y=["الطلب", "العرض"], title="منحنيات العرض والطلب")
    fig.add_scatter(x=[current_price], y=[demand_at_price], mode="markers", name="الطلب الحالي", marker=dict(color="blue", size=12))
    fig.add_scatter(x=[current_price], y=[supply_at_price], mode="markers", name="العرض الحالي", marker=dict(color="red", size=12))
    fig.update_layout(xaxis_title="السعر", yaxis_title="الكمية", legend_title="المنحنيات", title_x=0.5)

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"<div style='text-align:right; direction:rtl; font-size:18px; color:#333;'>{note}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h4 style='text-align:right; direction:rtl;'>🎓 خلاصة</h4>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:right; direction:rtl; font-size:18px;'>
    <ul>
    <li>إذا كان <strong>السعر مرتفعًا</strong>، يكون هناك <strong>فائض</strong> في السوق → السعر ينخفض.</li>
    <li>إذا كان <strong>السعر منخفضًا</strong>، يكون هناك <strong>نقص</strong> في السوق → السعر يرتفع.</li>
    <li>عند <strong>سعر التوازن</strong>، لا يوجد ضغط نحو الزيادة أو النقص.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
