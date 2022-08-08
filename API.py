# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
import requests
import pandas as pd
from flask import Flask, request
import urllib.request as urllib2


#Data

#Chargement Modèle
filename = 'DATA/model.sav'
model = pickle.load(open(filename, 'rb'))


#Chargement dataset

target_url="https://scoring-credit.s3.eu-west-3.amazonaws.com/df_Xvalidation.txt"
data = urllib2.urlopen(target_url) # it's a file like object and works just like a file
df = pd.read_csv(data, sep=',',index_col=0)
df=df.reset_index(drop=True)
df=df.iloc[:,0:]



#Application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bienvenue sur le modèle de scoring'

@app.route('/ID')
def hello_worldo():
    return 'ID du client'

@app.route('/ID/<ok>', methods=['GET'])
def hello_worlda(ok):
    ID=int(ok) #100194
    index=df[df["SK_ID_CURR"]==ID].index.values[0]
    proba=model.predict_proba(df.iloc[index:index+1,:])[0][1]
    return jsonify({'proba' : proba})



if __name__ == '__main__':
    app.run()
    
    
#Fin
