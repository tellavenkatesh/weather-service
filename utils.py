import requests
import pandas as pd
from database import get_db_connection

def fetch_weather_data(lat: float, lon: float):
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude=47.37&longitude=8.55&hourly=temperature_2m,relative_humidity_2m"
    
    )
    res = requests.get(url)
    data = res.json()
    timestamps = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]
    hums = data["hourly"]["relative_humidity_2m"]

    conn = get_db_connection()
    for t, temp, hum in zip(timestamps, temps, hums):
        conn.execute(
            "INSERT OR REPLACE INTO weather_data (timestamp, temperature, humidity) VALUES (?, ?, ?)",
            (t, temp, hum),
        )
    conn.commit()
    conn.close()
