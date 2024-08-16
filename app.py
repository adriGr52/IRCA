
import streamlit as st
import pandas as pd

# Leer el archivo de Excel
df = pd.read_excel('mockup_v2.xlsx')

# Título del dashboard
st.title('Mockup Dashboard')

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
