import streamlit as st
import pandas as pd

# ID del documento de Google Sheets
sheet_id = '1usXpjL3KAR3w5MwKYa1NZsz4WJtInJ6W'

# Formar la URL de exportación
csv_export_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'

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
