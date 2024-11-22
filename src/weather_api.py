import requests


def get_weather_data(latitud, longitud, forecast_type, rango_fechas):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitud,
        "longitude": longitud,
        "start_date": rango_fechas[0].strftime("%Y-%m-%d"),
        "end_date": rango_fechas[1].strftime("%Y-%m-%d"),
        "timezone": "auto",
    }

    if forecast_type == "Diario":
        params["daily"] = "temperature_2m_max,temperature_2m_min"
    elif forecast_type == "Por horas":
        params["hourly"] = (
            "temperature_2m,precipitation_probability,precipitation,wind_speed_10m"
        )

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error al conectar con la API: {e}")
