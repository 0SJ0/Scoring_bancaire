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

CURRENT_THEME = "light"
IS_DARK_THEME = False

st.set_page_config(layout="wide")



st.markdown("#  <center> :moneybag: Présentation du modèle :moneybag: </center> ", unsafe_allow_html=True)

st.sidebar.markdown("# 🎈 PRESENTATION MODELE ")

st.sidebar.markdown("Sur cette page, nous vulgarisons notre modèle.")

st.sidebar.markdown("<p style='text-align:center;'> <img src='https://cdn.dribbble.com/users/513906/screenshots/5384407/dribbb.gif' width='250' height='200'> </p>", unsafe_allow_html=True)



#Test
df=pd.read_csv("Data/Test.csv")
#SHAP
#filename = 'Data/model.sav'


model= pd.read_pickle(r'Data/model.sav')
#model = pickle.load(open(filename, 'rb'))

explainer = shap.TreeExplainer(model[1])
choosen_instance = df
shap_values = explainer.shap_values(choosen_instance)
st_shap(shap.summary_plot(shap_values,df,plot_size=[5*3,10*2]), height=1020,width=1300)
