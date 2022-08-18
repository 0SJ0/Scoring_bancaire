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
import pickle
import shap
from streamlit_shap import st_shap
import urllib.request as urllib2
import imblearn

CURRENT_THEME = "light"
IS_DARK_THEME = False

st.set_page_config(layout="wide")



st.sidebar.markdown("# 🎈 PAGE D'ACCUEIL ")

st.sidebar.markdown("Page d'accueil du dashboard. Ci-dessus le menu principal qui permet de découvrir notre modèle de scoring.")




st.sidebar.markdown("<p style='text-align:center;'> <img src='https://cdn.dribbble.com/users/513906/screenshots/5384407/dribbb.gif' width='250' height='200'> </p>", unsafe_allow_html=True)



#Michaël vous a fourni des spécifications pour le dashboard interactif. Celui-ci devra contenir au minimum les fonctionnalités suivantes :

#Permettre de visualiser le score et l’interprétation de ce score pour chaque client de façon intelligible pour une personne non experte en data science.
#Permettre de visualiser des informations descriptives relatives à un client (via un système de filtre).
#Permettre de comparer les informations descriptives relatives à un client à l’ensemble des clients ou à un groupe de clients similaires.

#Test
df=pd.read_csv("Data/Test.csv")
#st.dataframe(df.head())


#Présentation de l'application

st.markdown("#  <center> :moneybag: Score crédit :moneybag:  </center> ", unsafe_allow_html=True)

st.markdown("<p style='text-align: justify;'>Ce dashboard a pour objectif de diffuser notre outil de scoring de crédit. Sans compter la page d'accueil, il est divisé en 3 pages accesibles via le menu de gauche. Vous pouvez vous informer sur le modèle, réaliser une analyse micro ou macro d'un client.</p>", unsafe_allow_html=True)

#st.markdown("<p style='text-align: justify;'>Cet interface intéractif permmet de visualiser les informations descriptives et le score bancaire d'un client. Il est aussi possibles de comparer ces informations avec l'ensemble des clients ou à un groupe similaire.</p>", unsafe_allow_html=True)

image = Image.open('Images/Scoring.jpeg')
st.image(image, caption=" Notre score est basé sur la probabilité qu’un client rembourse son crédit à partir des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.). Il est compris entre 0 et 100. Plus il est proche de 100, plus l'individu est à risque.")



