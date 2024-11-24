import streamlit as st
import pandas as pd
import datetime
import os
from utility import paises  # Importa el módulo de países
from weather_api import get_weather_data  # Importa el módulo de la API

# Configuración de la aplicación
st.set_page_config(page_title="Pronóstico del Tiempo", page_icon="☀️", layout="centered")


# Crear una ruta compatible
base_dir = "images"
mini_logo = "logo_USS.png"
logo = "logo_USS_35.png"

logo = os.path.join(base_dir, logo)
mini_logo = os.path.join(base_dir, mini_logo)

# Título de la aplicación
st.title("🌦️ Aplicación del Tiempo - Open Meteo API")
st.logo(
    logo,
    link="https://www.uss.cl/",
    icon_image=mini_logo,
)

# Entrada de ubicación
st.sidebar.header("Configuración:")

# Selección del país
pais_seleccionado = st.sidebar.selectbox("Selecciona un país:", list(paises.keys()))

if pais_seleccionado:
    # Selección de la ciudad según el país seleccionado
    ciudad_seleccionada = st.sidebar.selectbox(
        "Selecciona una ciudad:", list(paises[pais_seleccionado].keys())
    )

    if ciudad_seleccionada:
        # Mostrar las coordenadas de la ciudad seleccionada
        coordenadas = paises[pais_seleccionado][ciudad_seleccionada]
        latitud = coordenadas["latitud"]
        longitud = coordenadas["longitud"]
    else:
        st.sidebar.error("Por favor selecciona una ciudad válida.")
        st.stop()
else:
    st.sidebar.error("Por favor selecciona un país válido.")
    st.stop()

# Fechas clave
today = datetime.date.today()
first_day_of_month = datetime.date(today.year, today.month, 1)
first_day_of_year = datetime.date(today.year, 1, 1)
last_day_of_year = datetime.date(today.year, 12, 31)

# Selector de rango de fechas
rango_fechas = st.sidebar.date_input(
    label="Selecciona un rango de fechas:",
    value=(first_day_of_month, today),
    min_value=first_day_of_year,
    max_value=last_day_of_year,
)

# Validación del rango de fechas
if len(rango_fechas) != 2 or rango_fechas[0] > rango_fechas[1]:
    st.sidebar.error("Por favor selecciona un rango de fechas válido.")
    st.stop()

# Tipo de pronóstico
forecast_type = st.sidebar.selectbox("Tipo de pronóstico:", ["Diario", "Por horas"])

# Obtener datos del clima
try:
    data = get_weather_data(latitud, longitud, forecast_type, rango_fechas)
except Exception as e:
    st.error(f"Error al obtener los datos del clima: {e}")
    st.stop()

# Mostrar los datos si existen
if data:
    if forecast_type == "Diario":
        st.subheader(f"🌞 Pronóstico Diario para {ciudad_seleccionada}.")
        daily_data = pd.DataFrame(data.get("daily", {}))
        if not daily_data.empty:
            st.line_chart(
                daily_data.set_index("time")[
                    ["temperature_2m_max", "temperature_2m_min"]
                ],
                x_label="Fecha",
                y_label="Temperatura. (Cº)",
            )
        else:
            st.warning("No hay datos disponibles para el rango de fechas seleccionado.")
    elif forecast_type == "Por horas":
        st.subheader(f"⏳ Pronóstico por Horas para {ciudad_seleccionada}.")
        hourly_data = pd.DataFrame(data.get("hourly", {}))
        if not hourly_data.empty:
            st.write("Temperatura.")
            st.line_chart(
                hourly_data.set_index("time")[["temperature_2m"]],
                x_label="Fecha",
                y_label="Temperatura. (Cº)",
                color="#FF5733",
            )
            st.write("Probabilidad de precipitación.")
            st.line_chart(
                hourly_data.set_index("time")[["precipitation_probability"]],
                x_label="Fecha",
                y_label="Probabilidad de precipitación (%)",
                color="#2ecc71",
            )
            st.write("Precipitación.")
            st.line_chart(
                hourly_data.set_index("time")[["precipitation"]],
                x_label="Fecha",
                y_label="Precipitación. (mm)",
                color="#bfc9ca",
            )
            st.write("Velocidad del viento.")
            st.line_chart(
                hourly_data.set_index("time")[["wind_speed_10m"]],
                x_label="Fecha",
                y_label="Velocidad del viento. (km/h)",
                color="#5d6d7e",
            )
        else:
            st.warning("No hay datos disponibles para el rango de fechas seleccionado.")
else:
    st.warning("No hay datos disponibles para el rango de fechas seleccionado.")


# Información adicional
st.write(
    """
    Esta aplicación utiliza la [API de Open-Meteo](https://open-meteo.com/) 
    para proporcionar pronósticos meteorológicos precisos y gratuitos.
    """
)
