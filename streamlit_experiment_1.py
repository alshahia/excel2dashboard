
import streamlit as st
import pandas as pd
""""
# First Task
Here is my first app with streamlit
"""
df = pd.DataFrame([[1,2],[33,4]])
df

"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)
st.write("# @ last")

dataframe = np.random.rand(5,20)
dataframe_pd =pd.DataFrame(dataframe,columns=(f"col {i}" for i in range(20)))
"normal"
st.dataframe(dataframe)
"with style"
st.dataframe(dataframe_pd.style.highlight_max(axis =0))
"static table"
st.table(dataframe_pd.style.highlight_max(axis =0))
"# Chart"
"line chart"
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)
st.line_chart(dataframe_pd)

"# plot map"
"San Francisco"
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)
"some map"
st.map(pd.DataFrame(np.array([[37.76, -122.4],[1,1]]),
                    columns=['lat', 'lon']))
"# Widgets"
"slider"
x= st.slider("x")
st.write(x,"squared is",x * x)
"text input "
st.text_input("your name",key ="name")
st.session_state.name

"# Check box"
if st.checkbox("show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=["a","b","c"]

    )
    chart_data

"# select box"
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
option = st.selectbox("which number do you like best?",
                      df["first column"])
"you selected",option

"# sidebar"
add_selectbox = st.sidebar.selectbox("how would you like be contacted?",
                                     ("email","Home phone","Mobile phone"))
add_slider = st.sidebar.slider(
    "select a range of value",0,100,(25,75)
)

path = "جدول ابو حسين - Copy.xlsx"
df = pd.read_excel(path,sheet_name="رواتب العمال",nrows=85,skiprows=2)
# pd =pd.drop(pd.columns[1])
del df[pd.columns[1]]
st.dataframe(df)
data_row =[]
for col in df.columns:
    for row in df[col]:
        data_row.append(row)
        break
"finsh first row"
data_row
for s,g in pd.items():
    s
    g
f =pd.transpose(copy =True)
f
data_row =[]
for col in f.columns:
    for row in f[col]:
        data_row.append(row)
        break
"finsh first row"
data_row
full_data =pd.DataFrame()
with  open("1.xlsx","a")as excel_writer:
    for s,g in f.items():
        full_data[s]=g
        # gg =pd.DataFrame(col=s).append(g)
    full_data