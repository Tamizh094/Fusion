
import pandas as pd
import streamlit as st

def st_selection(df,ipg,nLight):
    Laser_Make = st.sidebar.selectbox('Please Select Laser Make', options = df["Laser_Make"].unique())
    if Laser_Make == 'IPG':
        Laser_Model = st.sidebar.multiselect("Please Select Laser Model",options = ipg)
    else:
        Laser_Model = st.sidebar.multiselect("Please Select Laser Model", options = nLight)
    Material = st.sidebar.selectbox("Please Select Material Type",options = df['Material'].unique())
    Thickness = st.sidebar.multiselect("Please Select Material Thickness", options = df['Thickness'].unique())
    
    df_select = df.query("Laser_Make == @Laser_Make & Laser_Model == @Laser_Model & Material == @Material & Thickness == @Thickness")
    df_selection = df_select.transpose()
    df_selection.index.set_names('Details',inplace=True)
    df_selection.reset_index(inplace = True)
    st.dataframe(df_selection)
    