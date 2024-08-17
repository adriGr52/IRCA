
import streamlit as st
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')
import os

# Ruta a la carpeta de los documentos
folder_path = '/content/drive/My Drive/Prueba'

# Listar los archivos en la carpeta
files = os.listdir(folder_path)

# Ruta al archivo de Excel
file_path = os.path.join(folder_path, 'mockup_v2.xlsx')

# Leer el archivo Excel en un DataFrame
df = pd.read_excel(file_path)

# Título del dashboard
st.title('Mockup Dashboard desde Excel')

# Mostrar los datos en una tabla
st.subheader('Datos del archivo Excel')
st.dataframe(df)

# Gráfica simple
st.subheader('Gráfica de ejemplo')
st.line_chart(df.select_dtypes(include=['number']))

# Filtros interactivos
st.subheader('Filtrar datos')
column = st.selectbox('Selecciona una columna', df.columns)
unique_values = df[column].unique()
value = st.selectbox('Selecciona un valor', unique_values)
filtered_df = df[df[column] == value]
st.write(filtered_df)
