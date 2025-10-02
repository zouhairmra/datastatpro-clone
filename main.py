import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tableau de bord économique", layout="wide")
st.title("📊 Tableau de bord économique interactif")

# ---- 1. Chargement du modèle ML entraîné ----
st.sidebar.header("⚙️ Paramètres")
uploaded_model = st.sidebar.file_uploader("Charge ton modèle entraîné (.pkl)", type="pkl")

if uploaded_model is not None:
    model = joblib.load(uploaded_model)
    st.sidebar.success("Modèle chargé ✔️")
else:
    st.warning("Charge un modèle .pkl pour prédire.")

# ---- 2. Charger un fichier Excel (optionnel) ----
uploaded_data = st.file_uploader("Charge tes données économiques (.xlsx)", type="xlsx")

if uploaded_data is not None:
    df = pd.read_excel(uploaded_data)
    st.write("Aperçu des données :", df.head())

# ---- 3. Paramètres interactifs pour la prédiction ----
st.subheader("🔧 Paramètres du scénario")
col1, col2, col3 = st.columns(3)

with col1:
    taux_interet = st.slider("pib", 0.0, 15.0, 3.0)
with col2:
    invest_public = st.slider("inflation", 0.0, 500.0, 150.0)
with col3:
    croissance_pib = st.slider("chjomage", -5.0, 10.0, 2.0)

# ---- 4. Prédiction ----
if uploaded_model is not None and st.button("Prédire l'inflation"):
    X_new = pd.DataFrame([[taux_interet, invest_public, croissance_pib]],
                         columns=["Taux_interet", "Invest_Public", "Croissance_PIB"])
    prediction = model.predict(X_new)
    st.success(f"📈 Inflation prévue : **{prediction[0]:.2f}%**")

    # Exemple d'affichage graphique
    fig, ax = plt.subplots()
    ax.bar(["Inflation prévue"], [prediction[0]], color='skyblue')
    ax.set_ylabel("Inflation (%)")
    st.pyplot(fig)
else:
    st.info("Charge un modèle et clique sur Prédire.")

# ---- 5. Infos supplémentaires ----
st.sidebar.markdown("---")
st.sidebar.write("💡 **Astuce :** tu peux modifier les sliders pour tester plusieurs scénarios.")
