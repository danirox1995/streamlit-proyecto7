import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header('Mi primera app con Streamlit y Plotly')

# Leer datos (asegúrate de tener este archivo CSV en la misma carpeta)
car_data = pd.read_csv('vehicles_us.csv')

# Casilla para histograma
if st.checkbox('Mostrar histograma'):
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Casilla para gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión'):
    st.write('Creación de un gráfico de dispersión entre odómetro y precio')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)