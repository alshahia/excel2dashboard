import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import pandas as pd
import chardet

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


#ijln
ar_path_txt = r"اختبارات المواد الأولية(نقع).txt"
ar_path_csv = r"اختبارات المواد الأولية(نقع).csv"
temp_path =r"D:\python\python_project\excel2dashboard\1.txt"
ar_path =r"D:\python\python_project\excel2dashboard\اختبارات المواد الأولية(نقع).xlsx"
path = r"raw material tests (Soak ).xlsx"
#iconv -f cp1252 -t utf-8 -c D:\python\python_project\excel2dashboard\soak_result_arabic.csv -o D:\python\python_project\excel2dashboard\1.txt
with open(ar_path_csv,encoding='cp1252') as f:
        print(f.encoding)
        print(f.read().encode('utf-8').decode('cp1252'))
        #d =f.read()

        s=f.read().encode('utf-8').decode('cp1252')

        print(s)
with open(ar_path_csv,encoding='utf-8') as f:
        print(f.encoding)
        ss =f.read()
        csv_ss =pd.read_csv(f,skiprows=3)
        print(f.read().encode('cp1252').decode('utf-8'))
ss

#**************Solution
t ="\u0648\u062c\u0628\u0629"


t.encode('utf-8').decode('cp1252')

#***************

df_ar = pd.read_csv(ar_path_csv,skiprows=1,encoding='utf-8')

df_ar1 = pd.read_csv(ar_path_csv,skiprows=3,encoding='cp1252')
open(path)
pd.read_csv("اختبارات المواد الأولية(نقع).txt",)
# ---- READ EXCEL ----
df = pd.read_excel(
        io=path,
        engine="openpyxl",#XLRD ,ODF,PYXLSB,openpyxl

        skiprows=1,
        usecols="A:M", #A:P or A:N
        nrows=25,

    )
#print(df_ar.info)

st.dataframe(df_ar)

#read csv file


