#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:03:08 2022
@author: Oso
"""
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt







#


st.markdown("<h1 style='text-align: center;'> Score bancaire</h1>", unsafe_allow_html=True)


st.markdown("<p style='text-align: justify;'>Le métamatching a pour objectif d'estimer quantitativement l'effet causal d'un traitement en se basant sur plusieurs méthodes de matchings. La probabilité que l'individu reçoit le traitement peut être calculée à partir de plusieurs modèles de régressions ( logistiques ou régularisés) et l'appariement est aussi personnalisable. Notre objetif avec le métamatching est de proposer une approche ensembliste des modèles de matching pour construire la meilleure  estimation possible de l'effet causal d'un traitement sur une variable.</p>", unsafe_allow_html=True)







st.markdown("<h3 style='text-align: left; '>Initialisation</h3>", unsafe_allow_html=True)


     
st.markdown("<h3 style='text-align: left; color: purple;'>Références</h3>", unsafe_allow_html=True)

st.markdown("[[1] Noah Greifer( 2022),MatchIt: Getting Started](https://cran.r-project.org/web/packages/MatchIt/vignettes/MatchIt.html)",unsafe_allow_html=True)

st.markdown("[[2] Marco Caliendo (2005),Some Practical Guidance for the Implementation of Propensity Score Matching](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=721907)",unsafe_allow_html=True)

st.markdown("[[-] Osjo (2022), lien github du métamatching  ](https://github.com/0SJ0/Metamatching)",unsafe_allow_html=True)
