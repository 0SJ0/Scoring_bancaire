import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.graph_objects as go
import shap

#Test
df=pd.read_csv("Data/Test.csv")

st.markdown("#  <center> :moneybag: analyse micro :moneybag:  </center> ", unsafe_allow_html=True)


st.sidebar.markdown("# 🎈 ANALYSE MICRO ")

st.sidebar.markdown("Sur cette page, nous nous concentrons sur les caractéristiques individuelles de l'individu et les features locales qui jouent sur l'obtention ou non de son prêt.")

st.sidebar.markdown("<p style='text-align:center;'> <img src='https://cdn.dribbble.com/users/513906/screenshots/5384407/dribbb.gif' width='250' height='200'> </p>", unsafe_allow_html=True)


liste_clients=list(df.SK_ID_CURR.values)

ID_client = st.selectbox(
     'Sélectionne un client :',
     liste_clients)

st.write('You selected:',ID_client)

st.markdown("<h3 style='text-align: left; color: lightblue;'>Informations du client</h3>", unsafe_allow_html=True)

ligne=df[df.SK_ID_CURR==int(ID_client)][["SK_ID_CURR","CODE_GENDER","CNT_CHILDREN","AMT_INCOME_TOTAL"]]

st.write('ID :',ID_client)

Sexe=ligne.CODE_GENDER.values[0]

if Sexe :
    Sexe="Homme"
else :
    Sexe="Femme"

st.write("Sexe :",Sexe)

st.write("Nombre d'enfant :",ligne.CNT_CHILDREN.values[0])

st.write("Revenu total :",ligne.AMT_INCOME_TOTAL.values[0],"$")



#Prédiction du score

st.markdown("<h3 style='text-align: left; color: lightblue;'>Score</h3>", unsafe_allow_html=True)

score=70

fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = score,
    mode = "gauge+number+delta",
    title = {'text': "Credit score"},
    delta = {'reference': 50},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 50], 'color': "#F1CBA4"},
                 {'range': [50, 100], 'color': "lightgreen"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 50}}))

st.plotly_chart(fig, use_container_width=True)

