import json
import requests
from datetime import datetime

def handler(request, response):
    try:
        # Запрос к ipapi.co для получения информации о посетителе
        api_response = requests.get('https://ipapi.co/json/', timeout=5)
        api_response.raise_for_status()
        data = api_response.json()
    except requests.RequestException as e:
        print(f"Error fetching visitor info: {e}")
        data = {
            "ip": "N/A",
            "country_name": "N/A",
            "region": "N/A",
            "city": "N/A",
            "latitude": "N/A",
            "longitude": "N/A",
            "timezone": "N/A",
            "org": "N/A",
            "asn": "N/A",
            "postal": "N/A",
            "currency": "N/A",
            "languages": "N/A"
        }

    # Возвращаем данные в формате JSON
    return response.json({
        "ip": data.get("ip", "N/A"),
        "country_name": data.get("country_name", "N/A"),
        "region": data.get("region", "N/A"),
        "city": data.get("city", "N/A"),
        "latitude": data.get("latitude", "N/A"),
        "longitude": data.get("longitude", "N/A"),
        "timezone": data.get("timezone", "N/A"),
        "org": data.get("org", "N/A"),
        "asn": data.get("asn", "N/A"),
        "postal": data.get("postal", "N/A"),
        "currency": data.get("currency", "N/A"),
        "languages": data.get("languages", "N/A")
    })
