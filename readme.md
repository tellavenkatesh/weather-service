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


** To Run **
- git clone https://github.com/tellavenkatesh/weather-service.git
- cd weather-service
- pip install -r requirements.txt
- uvicorn app:app --reload


1. **Fetch & store weather data**
Example:
GET /weather-report?lat={latitude}&lon={longitude}
http://127.0.0.1:8000/weather-report?lat=47.37&lon=8.55

2. **Export Excel**
GET /export/excel
http://127.0.0.1:8000/export/excel
3. **Export PDF**
GET /export/pdf
http://127.0.0.1:8000/export/pdf
