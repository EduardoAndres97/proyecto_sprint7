import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Elige tu proximo vehículo') # Titulo de la app

st.write('Con nuestra aplicacion puedes ver los detalles de tu nuevo vehículo ideal') # Descripción de la app

casilla_transmision = st.checkbox('Transmisión') # crear casilla transmisión
casilla_color = st.checkbox('Color') # crear casilla color
casilla_estado = st.checkbox('Estado') #crear casilla estado

if casilla_transmision: # si la casilla de verificación está seleccionada
    st.write('Acá puedes ver la cantidad de vehículos que cuentan con transmisión automática o manual')
    fig = px.histogram(car_data, x="transmission",labels={"transmission": "Tipo de Transmisión"},title="Transmisión") # crear el gráfico
    st.plotly_chart(fig, use_container_width=True)


if casilla_color:
    st.write('Revisa los colores disponibles')
    fig = px.histogram(car_data,x= 'paint_color',labels={"paint_color": "Colores Disponibles"},title="Colores") # crear el gráfico
    st.plotly_chart(fig,use_container_width=True)

if casilla_estado:
    st.write('Revisa el estado de nuestros vehículos')
    fig = px.histogram(car_data,x= 'condition',labels={"condition": "Condiciones de los vehículos"},title="Estado de Nuestros Vehículos") #crear el gráfico
    st.plotly_chart(fig, use_container_width=True)
