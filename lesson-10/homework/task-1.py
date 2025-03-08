import requests
import os

base_url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = os.getenv('API_KEY')
coordinate_url = 'http://api.openweathermap.org/geo/1.0/direct'
if not api_key:
    raise ValueError('API KEY not found')

def finding_coordinate(city):
    coordinate = requests.get(coordinate_url+f'?q={city}&appid={api_key}')
    print(coordinate.status_code)
    data = coordinate.json()
    lat = data[0]['lat']
    lon = data[0]['lon']
    return lat, lon

def finding_temperature(lat, lon):
    temp = requests.get(base_url+f'?lat={lat}&lon={lon}&appid={api_key}')
    data = temp.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    return temperature, humidity

lat, lon = finding_coordinate('Tashkent')
tempature, humidity = finding_temperature(lat, lon) 
print(f"Temprature: {tempature}\nHumidity: {humidity}")