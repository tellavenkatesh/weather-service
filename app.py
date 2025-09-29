from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import pandas as pd
import matplotlib.pyplot as plt
import os
from database import init_db, get_db_connection
from utils import fetch_weather_data
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

app = FastAPI(title="Weather Report Service")

init_db()

@app.get("/weather-report")
def weather_report(lat: float = Query(...), lon: float = Query(...)):
    fetch_weather_data(lat, lon)
    return {"message": "Weather data fetched & stored."}

@app.get("/export/excel")
def export_excel():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 48", conn)
    file_path = "outputs/weather_data.xlsx"
    os.makedirs("outputs", exist_ok=True)
    df.to_excel(file_path, index=False)
    return FileResponse(file_path, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename="weather_data.xlsx")

@app.get("/export/pdf")
def export_pdf():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 48", conn)

    # Generate chart
    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["temperature"], label="Temperature (°C)", color="red")
    plt.plot(df["timestamp"], df["humidity"], label="Humidity (%)", color="blue")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    chart_path = "outputs/chart.png"
    plt.savefig(chart_path)
    plt.close()

    # Generate PDF with ReportLab
    pdf_path = "outputs/weather_report.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [
        Paragraph("Weather Report", styles["Title"]),
        Paragraph("Last 48 Hours Data", styles["Normal"]),
        Spacer(1, 20),
        Image(chart_path, width=400, height=200),
    ]
    doc.build(story)

    return FileResponse(pdf_path, media_type="application/pdf", filename="weather_report.pdf")
