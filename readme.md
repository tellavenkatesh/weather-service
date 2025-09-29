# Weather Report Service

A small backend service that fetches time-series weather data from Open-Meteo API, stores it in SQLite, and generates Excel & PDF reports.



## Features
- Fetch last 2 days of **temperature & humidity** data from Open-Meteo API.
- Store data in **SQLite** database.
- Export last 48 hours of data as **Excel** (`.xlsx`).
- Export a **PDF report** with a chart showing temperature & humidity.
- FastAPI endpoints for easy integration.
- Optional Docker support.



## Endpoints

1. **Fetch & store weather data**
