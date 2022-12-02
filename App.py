# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:03:57 2022

@author: Tamizharasan
"""

import pandas as pd
import streamlit as st
import Background

df = pd.read_excel("MasterDatabase.xlsx")

df['Date'] = df['Date'].dt.date

st.set_page_config(page_title='Machine Database', layout='wide', 
                   page_icon = None)

Background.image('bg.jpg')
                    
Page_names = ['About', 'View Data', 'Enter Data']
with st.sidebar.container():
    page = st.radio('Please Select options below', Page_names)
    
if page == 'About':
    st.write("""
             # Cutting Parameter Database:
             ### This web app contains cutting parameters of all the ***Machines***""")
             
elif page == 'View Data':
    st.subheader("Cutting Parameter database:")
    
    Machine = st.sidebar.multiselect('Please Select Machine Model', 
                             options = df['Machine'].unique()
                             )
    
    L_Make = st.sidebar.selectbox("Please Select Laser Make",
                                  options = df['L_Make'].unique())
    
    L_Model = st.sidebar.multiselect("Please Select Laser Model",
                                    options = df['L_Model'].unique())

    Material = st.sidebar.selectbox("Please Select Material Type",
                                      options= df['Material'].unique())
    
    Thickness = st.sidebar.multiselect("Please Select Material Thickness",
                                       options = df['Thickness'].unique())
    
    df_selection = df.query(
        "Machine == @Machine & Material == @Material& Thickness == @Thickness & L_Make == @L_Make & L_Model == @L_Model")
    
    df_selection = df_selection.transpose()
    df_selection.index.set_names("Details", inplace = True)
    df_selection.reset_index(inplace=True)
    
    

    
    st.dataframe(df_selection)
    
else:
    st.write("""## This Page is under development 
             ### This is entry page to enter values in it and save it in database""")
    
    
    
    