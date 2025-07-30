import json
import os
import requests

def lambda_handler(event, context):
    city = os.getenv('CITY', 'New York')
    api_key = os.getenv('API_KEY', 'demo')

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temp_c = data['current']['temp_c']

        return {
            "statusCode": 200,
            "body": json.dumps({
                "city": city,
                "temperature_celsius": temp_c
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
