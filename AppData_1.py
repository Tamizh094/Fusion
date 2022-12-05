import pandas as pd
import streamlit as st
import Background

df_1 = pd.read_excel("MasterDatabase.xlsx", sheet_name='Cutting')
df_2 = pd.read_excel("MasterDatabase.xlsx", sheet_name='Piercing')

df_1['Date'] = df_1['Date'].dt.date
#df_2['Date'] = df_2['Date'].dt.date
ipg = ['YLR 2.0/4.0 kW - HPP','YLR 3.0 kW', 'YLR 3.0/5.0 kW - HPP']
nLight = ['Corona CFX 4 kW', 'Standard CFL 4 kW', 'Corona CFX 5 kW']

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
    options = ['Cutting', 'Piercing']
    option = st.sidebar.radio("Please Select Data Option:", options)
    if option == 'Cutting':
        st.write("### Cutting Parameter database:")
    
        Machine = st.sidebar.multiselect('Please Select Machine Model', 
                             options = df_1['Machine'].unique())
                                             
    
        Laser_Make = st.sidebar.selectbox("Please Select Laser Make",
                                  options = df_1['Laser_Make'].unique(),
                                  )
        if Laser_Make == 'IPG':
    
            Laser_Model = st.sidebar.multiselect("Please Select Laser Model",
                                    options = ipg)
        else:
            Laser_Model = st.sidebar.multiselect("Please Select Laser Model", 
                                            options = nLight)

        Material = st.sidebar.selectbox("Please Select Material Type",
                                      options= df_1['Material'].unique())
    
        Thickness = st.sidebar.multiselect("Please Select Material Thickness",
                                       options = df_1['Thickness'].unique())
    
        df_selection = df_1.query(
            "Machine == @Machine & Material == @Material& Thickness == @Thickness & Laser_Make == @Laser_Make & Laser_Model == @Laser_Model")
    
        df_selection = df_selection.transpose()
        df_selection.index.set_names("Details", inplace = True)
        df_selection.reset_index(inplace=True)
        st.dataframe(df_selection)
    else:
        st.write("### Piercing Parameter DataBase:")
        
        
    
else:
    st.write("""## This Page is under development 
                This is the entry page to enter values on and save them in the database.""")
    
    
    
    
