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
x_axis = st.selectbox('select x element', el_list)
y_axis = st.selectbox('select y element', el_list)

st.multiselect('select location', file_name_list)     # to select more than one element
                                                                         # reboot app under manage app
colorlist = ['red', 'green', 'yellow', 'blue']

p = figure(x_axis_label=x_axis + ' [wt.%]', y_axis_label=y_axis + ' [wt.%]')

for i in range(len(file_name_list)):
  df2 = pd.read_csv(file_name_list[i])
  p.circle(df2[x_axis]/10000, df2[y_axis]/10000, color = colorlist[i])


#show(p)


st.bokeh_chart(p, use_container_width=True)
