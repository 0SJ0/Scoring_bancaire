import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.graph_objects as go

#Test
df=pd.read_csv("Data/Test.csv")

st.markdown("#  <h1 style='text-align: center; color: lightblue;'> :moneybag: Analyse micro :moneybag: </h1> ", unsafe_allow_html=True)

st.sidebar.markdown("# 🎈 ANALYSE MICRO ")

st.sidebar.markdown("Sur cette page, nous nous concentrons sur les caractéristiques individuelles de l'individu et les features locales qui jouent sur l'obtention ou non de son prêt.")

liste_clients=list(df.SK_ID_CURR.values)

ID_client = st.selectbox(
     'Sélectionne un client :',
     liste_clients)

