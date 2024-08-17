
import streamlit as st
import pandas as pd

# Cargar el archivo Excel desde la ruta donde se subió
file_path = '/mnt/data/mockup_v2.xlsx'
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
