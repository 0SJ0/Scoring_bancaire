import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.graph_objects as go
import shap
import requests
import pickle
from streamlit_shap import st_shap

#Test
df=pd.read_csv("Data/data.csv")

st.markdown("#  <center> :moneybag: Analyse micro :moneybag:  </center> ", unsafe_allow_html=True)


st.sidebar.markdown("# 🎈 ANALYSE MICRO ")

st.sidebar.markdown("Analyse micro ratachée à un client spéficique. On retrouves ses informations et son score crédit justifiée par une interprétabilité locale.")

st.sidebar.markdown("<p style='text-align:center;'> <img src='https://cdn.dribbble.com/users/513906/screenshots/5384407/dribbb.gif' width='250' height='200'> </p>", unsafe_allow_html=True)


liste_clients=list(df.SK_ID_CURR.values)

ID_client = st.selectbox(
     'Sélectionne un client :',
     liste_clients)


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

debut_requete="https://api-score-credit.herokuapp.com/ID/"
ID=str(ID_client)
requete_finale=debut_requete+ID
API_requete = requests.get(requete_finale)
#print(API_requete)
reponse=API_requete.json()
#print(reponse['Defaut_credit'])
score=round(reponse["Score"])

credit_accorde="Non"

if(reponse['Defaut_credit'])==0 : credit_accorde="Oui"

st.write("crédit accordé :",credit_accorde)



#Prédiction du score

st.markdown("<h3 style='text-align: left; color: lightblue;'>Score crédit</h3>", unsafe_allow_html=True)



fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = score,
    mode = "gauge+number",
    title = {'text': "Score crédit"},
    delta = {'reference': 50},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 60], 'color': "#91F792"},
                 {'range': [60, 100], 'color': "#EC5A5A"}],
             'threshold' : {'line': {'color': "red", 'width': 10}, 'thickness': 0.9, 'value': 30}}))

st.plotly_chart(fig, use_container_width=True)

st.markdown("<h3 style='text-align: left; color: lightblue;'>Interprétabilité locale</h3>", unsafe_allow_html=True)

index=int(df[df.SK_ID_CURR==ID_client].index.values)

logreg = pickle.load(open("Data/model.sav", 'rb'))
explainer = shap.KernelExplainer(logreg.predict_proba,shap.kmeans(df,3))
choosen_instance = df.loc[index]
shap_values = explainer.shap_values(choosen_instance)
#print(explainer.expected_value)
#print(choosen_instance)
#print(shap_values)
shap.initjs()
st_shap(shap.force_plot(explainer.expected_value[1], shap_values[1], choosen_instance), height=8000, width=1200)



