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
import imblearn
import base64
import urllib.request as urllib2

CURRENT_THEME = "light"
IS_DARK_THEME = False

st.set_page_config(layout="wide")



st.markdown("#  <center> :moneybag: Présentation du modèle :moneybag: </center> ", unsafe_allow_html=True)

st.sidebar.markdown("# 🎈 PRESENTATION MODELE ")

st.sidebar.markdown("Documentation sur notre modèle de scoring")

st.sidebar.markdown("<p style='text-align:center;'> <img src='https://cdn.dribbble.com/users/513906/screenshots/5384407/dribbb.gif' width='250' height='200'> </p>", unsafe_allow_html=True)

st.markdown("Ci-dessous un lien vers une note technique explicitant notre démarche de modélisation.")

image = Image.open('Images/Extrait_note.png')

st.image(image, "Une note conenant ...")
   

# Autres
st.markdown("<h3 style='text-align: left; color: lightblue;'>Références</h3>", unsafe_allow_html=True)

st.markdown("[[1] 10 Techniques to deal with Imbalanced Classes in Machine Learning](https://www.analyticsvidhya.com/blog/2020/07/10-techniques-to-deal-with-class-imbalance-in-machine-learning/)",unsafe_allow_html=True)

st.markdown("[[2] Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)",unsafe_allow_html=True)

st.markdown("[[-] Osjo (2022), lien github  ](https://github.com/0SJ0)",unsafe_allow_html=True)

