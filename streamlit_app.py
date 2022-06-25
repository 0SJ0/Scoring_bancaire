#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:03:08 2022
@author: Osjo
"""
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image



#Michaël vous a fourni des spécifications pour le dashboard interactif. Celui-ci devra contenir au minimum les fonctionnalités suivantes :

#Permettre de visualiser le score et l’interprétation de ce score pour chaque client de façon intelligible pour une personne non experte en data science.
#Permettre de visualiser des informations descriptives relatives à un client (via un système de filtre).
#Permettre de comparer les informations descriptives relatives à un client à l’ensemble des clients ou à un groupe de clients similaires.




#


st.markdown("<h1 style='text-align: center; color: lightblue;'> Score bancaire</h1>", unsafe_allow_html=True)

st.markdown("![ok](https://cdn.dribbble.com/users/238057/screenshots/4688471/comp-1_1.gif)")


st.markdown("<img src="https://cdn.dribbble.com/users/238057/screenshots/4688471/comp-1_1.gif" alt="Employee data" width="50" height="60" title="Employee Data title">")


st.markdown("<p style='text-align: justify;'>L'objectif est de déterminer si un client peut reçevoir un crédit à la consommation via un score. Cet interface intéractif permmet de visualiser les informations descriptives et le score bancaire d'un client. Il est aussi possibles de comparer ces informations avec l'ensemble des clients ou à un groupe similaire.</p>", unsafe_allow_html=True)



#st.markdown("<p style='text-align: justify;'>Cet interface intéractif permmet de visualiser les informations descriptives et le score bancaire d'un client. Il est aussi possibles de comparer ces informations avec l'ensemble des clients ou à un groupe similaire.</p>", unsafe_allow_html=True)


image = Image.open('Images/Scoring.jpeg')
st.image(image, caption=" L'outil 'scoring crédit' calcule la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé. Elle souhaite donc développer un algorithme de classification en s’appuyant sur des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.).")



st.markdown("<h3 style='text-align: left; color: lightblue;'>Données descriptives</h3>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: left; color: lightblue;'>Score</h3>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: left; color: lightblue;'>Comparaison</h3>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: left; color: lightblue;'>Références</h3>", unsafe_allow_html=True)

st.markdown("[[1] Noah Greifer( 2022),MatchIt: Getting Started](https://cran.r-project.org/web/packages/MatchIt/vignettes/MatchIt.html)",unsafe_allow_html=True)

st.markdown("[[2] Marco Caliendo (2005),Some Practical Guidance for the Implementation of Propensity Score Matching](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=721907)",unsafe_allow_html=True)

st.markdown("[[-] Osjo (2022), lien github du métamatching  ](https://github.com/0SJ0/Metamatching)",unsafe_allow_html=True)
