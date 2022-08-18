import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.graph_objects as go
import shap
from sklearn.neighbors import NearestNeighbors
import pickle
from streamlit_shap import st_shap

st.markdown("#  <center> :moneybag: Analyse macro :moneybag: </center> ", unsafe_allow_html=True)

st.sidebar.markdown("# 🎈 ANALYSE MACRO ")

st.sidebar.markdown("Analyse macro d'un client. Celui-ci est comparé relativement à l'ensemble des clients ou à des clients similaires.")

st.sidebar.markdown("<p style='text-align:center;'> <img src='https://cdn.dribbble.com/users/513906/screenshots/5384407/dribbb.gif' width='250' height='200'> </p>", unsafe_allow_html=True)

CURRENT_THEME = "light"
IS_DARK_THEME = False

st.set_page_config(layout="wide")

#Test
df=pd.read_csv("Data/data.csv")

samples = df.to_numpy()

neigh = NearestNeighbors(n_neighbors=31)
neigh.fit(samples)
result=neigh.kneighbors(df.iloc[1].to_numpy().reshape(1, -1))
df2 = df.filter(items = list(result[1][0])[1:], axis=0)
explainer = shap.KernelExplainer(logreg.predict_proba,shap.kmeans(df,3))
shap_values=explainer.shap_values(df2)
st_shap(shap.summary_plot(shap_values, features=df, plot_type='bar'))

