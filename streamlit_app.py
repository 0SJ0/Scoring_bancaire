#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:03:08 2022
@author: Osjo
"""

#Librairies utilisés
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.graph_objects as go



#Michaël vous a fourni des spécifications pour le dashboard interactif. Celui-ci devra contenir au minimum les fonctionnalités suivantes :

#Permettre de visualiser le score et l’interprétation de ce score pour chaque client de façon intelligible pour une personne non experte en data science.
#Permettre de visualiser des informations descriptives relatives à un client (via un système de filtre).
#Permettre de comparer les informations descriptives relatives à un client à l’ensemble des clients ou à un groupe de clients similaires.

#Test
df=pd.read_csv("Data/Test.csv")
#st.dataframe(df.head())


#Présentation de l'application
st.markdown("<h1 style='text-align: center; color: lightblue;'> Score crédit</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: justify;'>L'objectif est de déterminer si un client peut reçevoir un crédit à la consommation via un score. Cet interface intéractif permmet de visualiser les informations descriptives et le score bancaire d'un client. Il est aussi possibles de comparer ces informations avec l'ensemble des clients ou à un groupe similaire.</p>", unsafe_allow_html=True)

#st.markdown("<p style='text-align: justify;'>Cet interface intéractif permmet de visualiser les informations descriptives et le score bancaire d'un client. Il est aussi possibles de comparer ces informations avec l'ensemble des clients ou à un groupe similaire.</p>", unsafe_allow_html=True)

image = Image.open('Images/Scoring.jpeg')
st.image(image, caption=" L'outil 'scoring crédit' calcule la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé. Elle souhaite donc développer un algorithme de classification en s’appuyant sur des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.).")


# Information générale sur un client 

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


# Autres

st.write('Graphique explication score')

st.markdown("<h3 style='text-align: left; color: lightblue;'>Comparaison</h3>", unsafe_allow_html=True)

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=(["Client","Ensemble des clients","Clients similaires"]))

st.table(df)

st.markdown("<h3 style='text-align: left; color: lightblue;'>Références</h3>", unsafe_allow_html=True)

st.markdown("[[1] 10 Techniques to deal with Imbalanced Classes in Machine Learning](https://www.analyticsvidhya.com/blog/2020/07/10-techniques-to-deal-with-class-imbalance-in-machine-learning/)",unsafe_allow_html=True)

st.markdown("[[2] Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)",unsafe_allow_html=True)

st.markdown("[[-] Osjo (2022), lien github  ](https://github.com/0SJ0)",unsafe_allow_html=True)

st.markdown("<img src='https://cdn.dribbble.com/users/513906/screenshots/5384407/dribbb.gif'  align='middle' alt='Employee data' width='720' height='550' title='Employee Data title'>", unsafe_allow_html=True)
