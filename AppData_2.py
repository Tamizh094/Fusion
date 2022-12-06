
import pandas as pd
import streamlit as st
import Background as bg
import stquery

df_1 = pd.read_excel("MasterDatabase.xlsx", sheet_name='Cutting')
df_2 = pd.read_excel("MasterDatabase.xlsx", sheet_name='Piercing')
ipg = ['YLR 2.0/4.0 kW - HPP','YLR 3.0 kW', 'YLR 3.0/5.0 kW - HPP']
nLight = ['Corona CFX 4 kW', 'Standard CFL 4 kW', 'Corona CFX 5 kW']
df_1['Date'] = df_1['Date'].dt.date
df_2['Date'] = df_2['Date'].dt.date

st.set_page_config(page_title='Machine Database', layout='wide', 
                   page_icon = None)
                    
Page_names = ['About', 'View Data', 'Enter Data']
with st.sidebar.container():
    page = st.radio('Please Select options below', Page_names)
    
if page == 'About':
    st.write("""
             # Cutting Parameter Database:
             ### This web app contains cutting parameters of all the ***Machines***""")
             
elif page == 'View Data':
    bg.image('bg.jpg')
    options = ['Cutting', 'Piercing']
    option = st.sidebar.radio("Please Select Data Option:", options)
    if option == 'Cutting':
        st.write("### Cutting Parameter database:")
        stquery.st_selection(df_1, ipg, nLight)
    else:
        st.write("### Piercing Parameter DataBase:")
        stquery.st_selection(df_2, ipg, nLight)
        
else:
    bg.image('bg.jpg')
    st.write("""## This Page is under development 
                This is the entry page to enter values on and save them in the database.""")
    
    
    
    