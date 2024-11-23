# 🌦️ Aplicación del Tiempo - Open Meteo API

Esta es una aplicación de pronóstico del tiempo desarrollada con [Streamlit](https://streamlit.io/), utilizando la [API de Open-Meteo](https://open-meteo.com/). Proporciona pronósticos diarios y por horas para diferentes ciudades en varios países.

## 📋 Características

- Pronóstico meteorológico diario y por horas.
- Selección de países y ciudades preconfigurados.
- Rango de fechas personalizable.
- Gráficos interactivos para visualizar temperaturas y precipitaciones.

## 📂 Estructura del proyecto

```plaintext
Solemne3/
│
├── src/                        # Carpeta del codigo principal
│   └── app.py                  # Archivo principal de la aplicación Streamlit
│   └── weather_api.py          # Archivo del API
│   └── paises.py               # Lista de países y ciudades con sus coordenadas 
├── images/                     # Carpeta para imágenes
│   └── logo_USS_35.png         # Ejemplo de un logo
│   └── logo_USS.png            # Ejemplo de un logo
├── .streamlit                  # Archivo configuración de Streamlit
│   └── config.toml             # Configuración de Streamlit
├── requirements.txt            # Dependencias del proyecto
└── README.md                    # Documentación del proyecto

## Instalar dependencias:

Asegúrate de tener Python 3.7 o superior instalado. Luego, instala las dependencias:

```bash

pip install -r requirements.txt

## Ejecutar la aplicación:

```bash

streamlit run src\Principal.py

Esto abrirá la aplicación en tu navegador por defecto en http://localhost:8501.

## 🌎 Personalización:
Para personalizar la aplicación, puedes modificar el archivo `paises.py` para agregar o eliminar países

## 🛠️ Tecnologías utilizadas:

Python
Streamlit - Framework para crear aplicaciones web interactivas.
Open-Meteo API - Servicio gratuito para obtener datos meteorológicos.


## ⚙ Desarrollado por: 

·Margarita Améstica Fierro
·Yasna Becerra Almonacid
·Gastón Romero Riquelme
·Fransisca Ulloa Hermosilla
