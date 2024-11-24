# 🌦️ Aplicación del Tiempo y Quiz de Meteorología

## Descripción

Esta aplicación es un proyecto desarrollado con [Streamlit](https://streamlit.io/) que proporciona pronósticos del tiempo utilizando la [API de Open-Meteo](https://open-meteo.com/). Además, incluye un quiz interactivo para evaluar tus conocimientos sobre meteorología.

## 📋 Características

- Pronóstico meteorológico diario y por horas.
- Selección de países y ciudades preconfigurados.
- Rango de fechas personalizable.
- Gráficos interactivos para visualizar temperaturas y precipitaciones.
- Quiz de meteorología.

## 📂 Estructura del proyecto
```
    Solemne3/
    │
    ├── src/                        # Carpeta del código principal
    │   ├── app.py                  # Archivo principal de la aplicación Streamlit
    │   ├── weather_api.py          # Archivo del API para obtener datos meteorológicos
    │   ├── paises.py               # Lista de países y ciudades con sus coordenadas 
    │   ├── utility.py              # Funciones utilitarias y preguntas del quiz
    │   └── pages/                  # Carpeta para páginas adicionales
    │       └── quiz.py             # Página del quiz de meteorología
    ├── images/                     # Carpeta para imágenes
    │   ├── logo_USS_35.png         # Logo de la universidad
    │   └── logo_USS.png            # Logo adicional
    ├── .streamlit                  # Archivo de configuración de Streamlit
    │   └── config.toml             # Configuración de Streamlit
    ├── requirements.txt            # Dependencias del proyecto
    └── README.md                   # Documentación del proyecto
```

## 🌎 Personalización

Para personalizar la aplicación, puedes modificar el archivo `paises.py` para agregar o eliminar países y ciudades según tus preferencias. 

### Pasos para personalizar:

1. Abre el archivo `src/paises.py` en tu editor de texto o IDE.
2. Busca la sección donde están definidos los países y ciudades.
3. Para agregar un nuevo país, sigue el formato existente, por ejemplo:

```
    "Nuevo País 🇳🇱": {
       "Ciudad1": {"latitud": 12.3456, "longitud": 65.4321},
       "Ciudad2": {"latitud": 23.4567, "longitud": 76.5432},
    }
```
4. Para eliminar un país o ciudad, simplemente borra la sección correspondiente.
5. Guarda los cambios y vuelve a ejecutar la aplicación para ver las modificaciones reflejadas.

## 🛠️ Tecnologías utilizadas

- **Python**: Lenguaje de programación utilizado para el desarrollo.
- **Streamlit**: Framework para crear aplicaciones web interactivas.
- **Open-Meteo API**: Servicio gratuito para obtener datos meteorológicos.

## ⚙️ Instalación

1. Asegúrate de tener Python 3.7 o superior instalado en tu sistema.
2. Clona este repositorio en tu máquina local.
3. Navega al directorio del proyecto y ejecuta el siguiente comando para instalar las dependencias:

```
    pip install -r requirements.txt
```
## 🚀 Ejecución de la aplicación

Para ejecutar la aplicación, utiliza el siguiente comando en tu terminal:
    
```
    streamlit run src/Principal.py
```

Esto abrirá la aplicación en tu navegador por defecto en http://localhost:8501.

## ⚙ Desarrollado por: 

- Margarita Améstica Fierro.
- Yasna Becerra Almonacid.
- Gastón Romero Riquelme.
- Francisca Ulloa Hermosilla.
