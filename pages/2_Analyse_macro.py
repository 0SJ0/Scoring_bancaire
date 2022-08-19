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

def jitter(values,j):
    return values + np.random.normal(j,0.01,values.shape)


st.markdown("#  <center> :moneybag: Analyse macro :moneybag: </center> ", unsafe_allow_html=True)

st.sidebar.markdown("# 🎈 ANALYSE MACRO ")

st.sidebar.markdown("Analyse macro d'un client. Celui-ci est comparé relativement à l'ensemble des clients ou à des clients similaires.")

st.sidebar.markdown("<p style='text-align:center;'> <img src='https://cdn.dribbble.com/users/513906/screenshots/5384407/dribbb.gif' width='250' height='200'> </p>", unsafe_allow_html=True)



#Test
df=pd.read_csv("Data/data.csv")
logreg = pickle.load(open("Data/model.sav", 'rb'))

explainer = shap.KernelExplainer(logreg.predict_proba,shap.kmeans(df,3))




df3=df
df3["SCORE"]=[round(i*100) for i in logreg.predict_proba(df3)[:,1]]
####
df3.loc[df3['SCORE'] > 70, 'ACCORD_CREDIT'] = "Risque de défaut"  
df3.loc[df3['SCORE'] <= 70, 'ACCORD_CREDIT'] = 'Crédit accordé' 

liste_clients=list(df.SK_ID_CURR.values)

ID_client = st.selectbox(
     'Sélectionne un client :',
     liste_clients)

st.markdown("<h3 style='text-align: left; color: lightblue;'>Interprétabilité globale</h3>", unsafe_allow_html=True)

df=pd.read_csv("Data/data.csv")
samples=df.to_numpy()
neigh = NearestNeighbors(n_neighbors=6)
neigh.fit(samples)
result=neigh.kneighbors(df[df.SK_ID_CURR==int(ID_client)].to_numpy().reshape(1, -1))
df2 = df.filter(items = list(result[1][0])[1:], axis=0)
explainer = shap.KernelExplainer(logreg.predict_proba,shap.kmeans(df,3))
shap_values=explainer.shap_values(df2)
st_shap(shap.summary_plot(shap_values, features=df, plot_type='bar'), height=1000, width=1200)


samples = df.to_numpy()

st.markdown("<h3 style='text-align: left; color: lightblue;'>Distribution d'une variable qualitative</h3>", unsafe_allow_html=True)

df_type=df.loc[:, df.columns != 'SK_ID_CURR']
df_int=df_type.select_dtypes(include=['int64'])


df_float=df_type.select_dtypes(include=['float64'])


Col_qual = st.selectbox(
     'Sélectionne une colonne qualitative :',
     list(df_int.columns))

fig = plt.figure(figsize=(10, 4))#figsize=(10, 4)
sns.countplot(x =df3["ACCORD_CREDIT"],hue=df3[Col_qual])

pos=0
position=df3[df3.SK_ID_CURR==ID_client]["ACCORD_CREDIT"]
if(position.values=="Crédit accordé") : 
    pos=1

plt.scatter(x=[pos],y=[600],marker = ",",c="purple",s=222)
st.pyplot(fig)


st.markdown("<h3 style='text-align: left; color: lightblue;'>Distribution d'une variable quantitative</h3>", unsafe_allow_html=True)

Col_quant = st.selectbox(
     'Sélectionne une colonne quantitative:',
     list(df_float.columns))


fig2 = plt.figure(figsize=(10, 4))#figsize=(10, 4)
ax = sns.boxplot(x=df3["ACCORD_CREDIT"], y=df3[Col_quant])

val=df3[df3.SK_ID_CURR==ID_client][Col_quant]
plt.scatter(x=[pos],y=[val.values],marker = ",",c="purple",s=222)
st.pyplot(fig2)



st.markdown("<h3 style='text-align: left; color: lightblue;'>Analyse bivariée</h3>", unsafe_allow_html=True)

fig3 = plt.figure(figsize=(10, 4))#figsize=(10, 4)
sns.scatterplot(x = jitter(df3[Col_quant],2), 
                y = jitter(df3[Col_qual],2),
                hue=df3["SCORE"],s=200,alpha=0.5)

val1=df3[df3.SK_ID_CURR==ID_client][Col_qual]
val2=df3[df3.SK_ID_CURR==ID_client][Col_quant]

plt.scatter(x=[val2],y=[val1],marker = ",",c="purple",s=222)
st.pyplot(fig3)




