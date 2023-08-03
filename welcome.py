import streamlit as st
import pandas as pd
import os

file_name_list = []                   # initialisation: give a value to variable
for i in os.listdir():      # select each i in the directory (each .csv file)
  if i.endswith('csv'):
    file_name_list.append(i)

st.write('file_name_list')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)

st.multiselect('select location', file_name_list)
