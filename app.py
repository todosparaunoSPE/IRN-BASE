# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:22:08 2023

@author: jperezr
"""

#import json

import requests  # pip install requests
import streamlit as st  # pip install streamlit
import streamlit.components.v1 as components
#from streamlit_lottie import st_lottie  # pip install streamlit-lottie

import streamlit.web.cli 



#def load_lottieurl(url: str):
#    r = requests.get(url)
#    if r.status_code != 200:
#        return None
#    return r.json()



##lottie_hello = load_lottieurl("https://lottie.host/6f4ee854-3625-4849-8985-e423a0752949/hZWZsrb0zk.json")
   
#lottie_hello = load_lottieurl("https://lottie.host/f270a53f-1258-4846-9dd8-302fb8501c92/lxcu0ETdKd.json")

##lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_UJNc2t.json")



#st.title("Subdirección de Planeación Estratégica")


#st_lottie(lottie_hello, key = "hello")

#st.subheader("Tablas y grágicos")



st.subheader("INDICADOR DE RENDIMIENTO NETO DE LAS SIEFORES")
st.header("IRN")

st.subheader(" ")
st.subheader(" ")


#st.subheader("ene-2020 a sep-2023.")

###st.subheader("INTRODUCCIÓN.")


###st.markdown('<div style="text-align: justify;"><H3>Con el objetivo de dar seguimiento a la Acción puntual 2.3.4. Incentivar las aportaciones voluntarias de las y los trabajadores a sus fondos de retiro, de la Estrategia prioritaria 2.3 del Programa Institucional del Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado (ISSSTE) 2020-2024 , el Fondo Nacional de Pensiones de los Trabajadores al Servicio del Estado (PENSIONISSSTE) presenta un estudio prospectivo sobre el perfil de los cuentahabientes próximos al retiro que tienen una Cuenta individual actualmente en el Fondo.</H3></div>', unsafe_allow_html=True)



st.subheader("")
st.subheader("")




st.sidebar.success("Seleccione una página de arriba.")

#if "my_input" not in st.session_state:
#    st.session_state["my_input"] = ""

#my_input = st.text_input("Inroducir un texto aquí", st.session_state["my_input"])
#submit = st.button("Submit")
#if submit:
#    st.session_state["my_input"] = my_input
#    st.write("You have entered: ", my_input)