import pandas as pd
import streamlit as st
import plotly.express as px

df_vehiculos = pd.read_csv('./vehicles_us.csv')

# Boton del histograma kilometraje
hist_button = st.button('Construir histograma del kilometraje') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.header('distribución del kilometraje')
    st.write('Variable odometer')               
    # crear un histograma de odomoter
    fig = px.histogram(df_vehiculos, x="odometer")            
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



# Boton del histograma año del modelo
hist_button = st.button('Construir histograma del año del modelo') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.header('distribución del año del modelo')
    st.write('Variable model_year')               
    # crear un histograma de odomoter
    fig = px.histogram(df_vehiculos, x="model_year")            
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Boton del gráfico de dispersión de model_year y price
hist_button = st.button('Construir gráfico de dispersión del año del modelo y precio') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.header('Dispersión de la variable año del modelo y precio')
    st.write('Variables model_year y price')               
    # crear un gráfico de dispersión
    fig = px.scatter(df_vehiculos, x="model_year", y="price")            
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Boton del gráfico de dispersión de odometer y price
hist_button = st.button('Construir gráfico de dispersión del kilometraje y precio') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.header('Dispersión de la variable kilometraje  y precio')
    st.write('Variables odometer y price')               
    # crear un gráfico de dispersión
    fig = px.scatter(df_vehiculos, x="odometer", y="price")            
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)





