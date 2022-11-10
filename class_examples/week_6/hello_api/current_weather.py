import requests
from pprint import pprint
import os

# TODO this key works, but for some reason the program is unable to grab it from system environment variables
key = os.environ.get('WEATHER_KEY')
print(key)

user_country = input('Enter the two letter code of a country: ')
user_city = input('Enter the name of a city in that country: ')

user_city_country = f'{user_city},{user_country}'

url = f'https://api.openweathermap.org/data/2.5/weather'
query = {'q': user_city_country, 'units': 'celsius', 'appid': key} # to simplify url, and control individual variables in the query more easily


data = requests.get(url, params=query).json()

pprint(data)

temp = data['main']['temp']
print(f'The temperature in Minneapolis is {temp}F')