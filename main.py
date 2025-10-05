# app.py
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="EconMath - Applis")

st.title("EconMath — Applications mathématiques pour l'économie")
st.write("Simulateur et explications interactives pour comprendre l'offre, la demande, l'élasticité...")

# Sidebar navigation
page = st.sidebar.selectbox("Aller à", ["Accueil", "Offre-Demande", "Elasticité", "Explique (LLM local)"])

########################
# Accueil
########################
if page == "Accueil":
    st.header("Bienvenue")
    st.markdown("""
    - Utilise les pages pour explorer des concepts économiques via des simulations.
    - Option LLM local : obtenir des explications textuelles (voir page 'Explique').
    """)

########################
# Offre - Demande
########################
if page == "Offre-Demande":
    st.header("Simulateur Offre — Demande")
    st.markdown("Définis les fonctions linéaires : demande P = a - bQ ; offre P = c + dQ")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Paramètres Demande")
        a = st.number_input("a (intercept demande)", value=100.0, step=1.0)
        b = st.number_input("b (pente demande)", value=1.0, step=0.1)
    with col2:
        st.subheader("Paramètres Offre")
        c = st.number_input("c (intercept offre)", value=10.0, step=1.0)
        d = st.number_input("d (pente offre)", value=0.5, step=0.1)

    # Calcul équilibre linéaire: a - bQ = c + dQ -> Q* = (a - c) / (b + d)
    if b + d == 0:
        st.error("b + d ne peut pas être 0")
    else:
        Q_star = (a - c) / (b + d)
        P_star = a - b * Q_star
        st.metric("Quantité d'équilibre Q*", f"{Q_star:.3f}")
        st.metric("Prix d'équilibre P*", f"{P_star:.3f}")

        # Construction des courbes
        Q = np.linspace(0, max(0, Q_star*2), 200)
        P_d = a - b * Q
        P_s = c + d * Q

        fig, ax = plt.subplots()
        ax.plot(Q, P_d, label="Demande P=a-bQ")
        ax.plot(Q, P_s, label="Offre P=c+dQ")
        ax.scatter([Q_star], [P_star], color="red", zorder=5)
        ax.annotate(f"Equilibre\nQ={Q_star:.2f}\nP={P_star:.2f}", xy=(Q_star, P_star), xytext=(Q_star*0.6, P_star+5),
                    arrowprops=dict(arrowstyle="->"))
        ax.set_xlabel("Quantité Q")
        ax.set_ylabel("Prix P")
        ax.legend()
        st.pyplot(fig)

        # option export
        df = pd.DataFrame({"Q": Q, "P_demande": P_d, "P_offre": P_s})
        st.download_button("Télécharger les données (CSV)", df.to_csv(index=False), "supply_demand.csv", "text/csv")

########################
# Elasticité
########################
if page == "Elasticité":
    st.header("Calculatrice d'élasticité-prix de la demande (point & arc)")
    P1 = st.number_input("Prix initial P1", value=10.0)
    P2 = st.number_input("Prix final P2", value=12.0)
    Q1 = st.number_input("Quantité initiale Q1", value=100.0)
    Q2 = st.number_input("Quantité finale Q2", value=80.0)

    # Elasticité arc
    if P1*Q1 == 0:
        st.warning("P1*Q1 must be non-zero for arc elasticity")
    else:
        e_arc = ((Q2 - Q1) / ((Q2 + Q1)/2)) / ((P2 - P1) / ((P2 + P1)/2))
        st.write(f"Elasticité arc (prix) = {e_arc:.3f}")

    # Elasticité point approximation (dQ/dP approx)
    if (P2 - P1) != 0:
        slope = (Q2 - Q1) / (P2 - P1)
        e_point = slope * (P1 / Q1)
        st.write(f"Elasticité point (approx) = {e_point:.3f}")

########################
# Explique (intégration LLM local - optionnel)
########################
if page == "Explique (LLM local)":
    st.header("Explique-moi (LLM local, optionnel)")
    st.write("Pose une question conceptuelle ; le LLM local répondra (si installé).")
    prompt = st.text_area("Question :", value="Qu'est-ce que l'élasticité-prix de la demande ?")
    if st.button("Obtenir explication (local LLM)"):
        st.info("Tentative d'appel au LLM local (gpt4all ou llama)...")
        # --- Utilisation conditionnelle : si gpt4all installé, on l'utilise ---
        try:
            from gpt4all import GPT4All
            model = GPT4All("ggml-gpt4all-j.bin")  # adapter au modèle que tu as
            resp = model.generate(prompt)
            st.write(resp)
        except Exception as e:
            st.error("LLM local non disponible. Installer gpt4all et charger un modèle ggml/gguf.")
            st.write("Erreur :", e)
