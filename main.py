import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px
import numpy as np

# GPT4All imports
# from gpt4all import GPT4All  # décommente si GPT4All est installé

# --- Chargement des données ---
df = pd.read_csv("data/pib.csv", parse_dates=['Date'])
df.sort_values('Date', inplace=True)

st.title("Portfolio IA pour l'économie")

# --- Sélection de pays ou indicateur (si dataset multi-pays) ---
# Pour cet exemple, nous avons une seule série
st.subheader("Prévisions du PIB")

# --- Modèle Prophet ---
if st.button("Lancer la prévision"):
    m = Prophet()
    df_prophet = df.rename(columns={"Date":"ds","PIB":"y"})
    m.fit(df_prophet)
    future = m.make_future_dataframe(periods=8, freq='Q')
    forecast = m.predict(future)
    
    fig = px.line(forecast, x='ds', y='yhat', title='Prévision du PIB avec Prophet')
    fig.add_scatter(x=df['Date'], y=df['PIB'], mode='lines', name='Données réelles')
    st.plotly_chart(fig)

# --- Question à GPT4All ---
st.subheader("Assistant IA pour les données économiques")
user_question = st.text_input("Posez une question sur le PIB :")

if user_question:
    st.write("Réponse IA :")
    # Exemple pseudo-code pour GPT4All
    """
    gpt = GPT4All("models/gpt4all_model.bin")
    prompt = f"Données PIB : {df.head(20).to_dict()}\nQuestion : {user_question}"
    response = gpt.generate(prompt)
    st.write(response)
    """
    st.write("Réponse générée par GPT4All ici (exemple)")

# --- Statistiques descriptives ---
st.subheader("Statistiques de base")
st.write(df.describe())
