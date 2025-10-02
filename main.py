import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Analyse Éco ML", layout="wide")

st.title("📊 Plateforme Économique Interactive (ML)")

# --- 1. Upload des données ---
st.sidebar.header("1️⃣ Charger vos données Excel")
uploaded_file = st.sidebar.file_uploader("Fichier Excel (.xlsx)", type=["xlsx"])
sheet = st.sidebar.text_input("Nom de la feuille", value="Sheet1")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name=sheet)
    st.write("Aperçu des données :")
    st.dataframe(df.head())
else:
    st.info("Veuillez importer un fichier Excel.")
    st.stop()

# --- 2. Choix mode : Régression ou Clustering ---
mode = st.sidebar.radio("2️⃣ Choisir l'analyse :", ["Régression (prédiction)", "Clustering (segmentation)"])

# --- 3. Paramètres Régression ---
if mode == "Régression (prédiction)":
    target = st.sidebar.selectbox("Variable à prédire (y)", df.columns)
    features = st.sidebar.multiselect("Variables explicatives (X)", [c for c in df.columns if c != target])

    if len(features) > 0:
        # pipeline
        X = df[features]
        y = df[target]

        imputer = SimpleImputer(strategy='median')
        scaler = StandardScaler()
        model = Ridge(alpha=1.0)

        pipe = Pipeline([
            ('imputer', imputer),
            ('scaler', scaler),
            ('ridge', model)
        ])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        pipe.fit(X_train, y_train)
        score = pipe.score(X_test, y_test)

        st.subheader("⚙️ Modèle de Régression entraîné")
        st.write(f"R² sur test = {score:.2f}")

        # --- Scénarios interactifs ---
        st.subheader("📝 Scénario interactif")
        inputs = {}
        for f in features:
            minv, maxv = float(df[f].min()), float(df[f].max())
            val = st.slider(f"{f}", minv, maxv, float(df[f].mean()))
            inputs[f] = val

        new_data = pd.DataFrame([inputs])
        pred = pipe.predict(new_data)[0]
        st.success(f"Prévision de {target} = {pred:.2f}")

        st.caption("Déplacez les curseurs pour simuler différents scénarios macroéconomiques.")

# --- 3bis. Paramètres Clustering ---
else:
    features = st.sidebar.multiselect("Variables pour le clustering", df.columns)
    k = st.sidebar.slider("Nombre de clusters (k)", 2, 8, 3)

    if len(features) > 0:
        X = df[features].copy()
        X_scaled = StandardScaler().fit_transform(SimpleImputer(strategy='median').fit_transform(X))

        km = KMeans(n_clusters=k, random_state=42).fit(X_scaled)
        df['Cluster'] = km.labels_

        st.subheader("📍 Résultat du clustering")
        st.write(df[['Cluster'] + features].head())

        # visualisation
        if len(features) >= 2:
            plt.figure(figsize=(6, 4))
            sns.scatterplot(x=df[features[0]], y=df[features[1]], hue=df['Cluster'], palette="Set2")
            plt.xlabel(features[0])
            plt.ylabel(features[1])
            plt.title("Clustering")
            st.pyplot(plt)

        st.caption("Les clusters regroupent des observations économiquement proches.")

