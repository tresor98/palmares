import streamlit as st 
import pandas as pd 


st.write("""
# Lycee du Saint Esprit finalistes depuis 1958
	""")

selected_year = st.sidebar.selectbox('Year',list((range(1958,2020)))) 

data = pd.read_excel('Palmares.xlsx')

st.write(data[data["Date d'adieu"].dt.year== int(selected_year)])
st.write(selected_year)
