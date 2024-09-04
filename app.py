import pandas as pd
import streamlit as st
import plotly.express as px

df_vehiculos = pd.read_csv('./vehicles_us.csv')

#fig.show() # crear gráfico

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
# escribir un mensaje
st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')               
# crear un histograma de odomoter
fig = px.histogram(df_vehiculos, x="odometer")            
# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)



