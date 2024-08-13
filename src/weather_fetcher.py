from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
CITY = os.getenv('CITY')

def get_weather():
    params = {
        'q': CITY,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        return data['main']['temp'], data['weather'][0]['description']
    else:
        raise Exception(f"Error fetching weather data: {data['message']}")
