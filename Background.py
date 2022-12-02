# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:27:19 2022

@author: Tamizharasan
"""
import base64
import streamlit as st

def image(image_file):
     with open(image_file,"rb") as image_file:
         encoded_string = base64.b64encode(image_file.read())
     st.markdown(f"""
                 <style>
                 .stApp{{
                     background-image: url(data:image/{'jpg'};base64,{encoded_string.decode()});
                     background-size:cover;
                 }}
                 </style>""", unsafe_allow_html = True)