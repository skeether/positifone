import json
import requests
from datetime import datetime

def handler(request, response):
    try:
        # Запрос к ipinfo.io с API-ключом
        api_key = "5eaae20151b40c"  # Замени на твой ключ
        api_response = requests.get(f'https://ipinfo.io/json?token={api_key}', timeout=5)
        api_response.raise_for_status()
        data = api_response.json()
    except requests.RequestException as e:
        print(f"Error fetching visitor info: {e}")
        data = {
            "ip": "N/A",
            "country": "N/A",
            "region": "N/A",
            "city": "N/A",
            "loc": "N/A,N/A",  # latitude,longitude
            "timezone": "N/A",
            "org": "N/A",
            "asn": {"asn": "N/A"},
            "postal": "N/A"
        }

    # Извлечение данных, включая координаты
    loc = data.get("loc", "N/A,N/A").split(",")
    latitude = loc[0] if len(loc) > 0 else "N/A"
    longitude = loc[1] if len(loc) > 1 else "N/A"
    asn = data.get("asn", {}).get("asn", "N/A")

    # Возвращаем данные в формате JSON
    return response.json({
        "ip": data.get("ip", "N/A"),
        "country_name": data.get("country", "N/A"),
        "region": data.get("region", "N/A"),
        "city": data.get("city", "N/A"),
        "latitude": latitude,
        "longitude": longitude,
        "timezone": data.get("timezone", "N/A"),
        "org": data.get("org", "N/A"),
        "asn": asn,
        "postal": data.get("postal", "N/A"),
        "currency": "N/A",  # ipinfo не предоставляет валюту
        "languages": "N/A"   # ipinfo не предоставляет языки
    })
