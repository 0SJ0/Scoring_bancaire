# Import libraries
import numpy 
from flask import Flask, request, jsonify
import gunicorn
import fsspec
import pickle
import imblearn
import pandas as pd
#import urllib.request as urllib2
#import requests

#S3 connexion
#Téléchargement data plus modèle
S3_connexion=0




    
try :
    #df = pd.read_csv("Data/data.csv",index_col=0).reset_index(drop=True)
    df = pd.read_csv("Data/data.csv").reset_index(drop=True)

    S3_connexion+=1
except :
    print("Erreur")   
    
try :
    model = pd.read_pickle("Data/model.sav.zip",compression='infer')
    S3_connexion+=1
except :
    print("Erreur")
    
try :
    model = pickle.load(open('Data/model.sav', 'rb')  )
    S3_connexion+=1
except :
    print("Erreur")
   
    
model = pd.read_pickle("Data/model.sav")

    

#Application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bienvenue sur le modèle de scoring'

@app.route('/ID')
def ID():
    return 'ID du client'

@app.route('/ID/<id>', methods=['GET'])
def Prediction(id):
    try :
        ID=int(id) #100194
        index=df[df["SK_ID_CURR"]==ID].index.values[0]
        score=round(model.predict_proba(df.iloc[index:index+1,:])[0][1]*100) #368305
        defaut_credit=0
        if (score>30) : defaut_credit=1
        return jsonify({'Score' : score, "Defaut_credit" : defaut_credit})
    except :
        return jsonify({"erreur" : S3_connexion})
    
    
   


if __name__ == '__main__':
    app.run()
    
    
#Fin
