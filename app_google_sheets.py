
import streamlit as st
import pandas as pd

# URL de la hoja de Google Sheets (con enlace compartido)
sheet_url = 'https://docs.google.com/spreadsheets/d/1usXpjL3KAR3w5MwKYa1NZsz4WJtInJ6W/edit?usp=drive_link&ouid=109358120796349146990&rtpof=true&sd=true'

# Convertir la URL para obtener el formato adecuado para Pandas
csv_export_url = sheet_url.replace('/edit?usp=drive_link&ouid=109358120796349146990&rtpof=true&sd=true', '/export?format=csv')

# Leer los datos directamente desde Google Sheets
df = pd.read_csv(csv_export_url)

# Título del dashboard
st.title('Mockup Dashboard desde Google Sheets')

# Mostrar los datos en una tabla
st.subheader('Datos del archivo Google Sheets')
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
