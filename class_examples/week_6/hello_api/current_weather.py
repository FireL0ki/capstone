import requests
from pprint import pprint

url = 'https://api.openweathermap.org/data/2.5/weather?q=minneapolis,mn,us&units=imperial&appid=fb94f018c382e75efcfc009a97284108'

data = requests.get(url).json()

pprint(data)

temp = data['main']['temp']
print(f'The temperature in Minneapolis is {temp}F')