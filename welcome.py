import streamlit as st
import pandas as pd
import os
from bokeh.plotting import figure

file_name_list = []                   # initialisation: give a value to variable
for i in os.listdir():                # select each i in the directory (each .csv file)
  if i.endswith('csv'):
    file_name_list.append(i)

st.write(file_name_list)

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)

st.multiselect('select location', file_name_list, file_name_list[0])    # to select more than one element


x = [1, 2, 3, 4, 5]            # reboot app under manage app
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
