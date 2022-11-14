import requests
from pprint import pprint
import os

key = os.environ.get('WEATHER_KEY')
print(key) # for use during development / testing

def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print('Sorry, could not get weather')
    else:
        current_temp = get_temp(weather_data)
        print(f'The current temperature is {current_temp}')


def get_location():
    city, country = '', ''
    # error handling -- catching empty strings; make sure user enters a value
    while len(city) == 0:
        city = input('Enter the name of the city: ').strip()

    while len(country) == 0:
        country = input('Enter the two letter code of a country: ')

    location = f'{city},{country}'
    return location


def get_current_weather(location, key):
    url = f'https://api.openweathermap.org/data/2.5/weather'
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status() # riase exception for 400 or 500 errors
        data = response.json() # this may error too, if response is not JSON
        return data, None # will return none if this errors
    except Exception as ex:
        print(ex)
        print(response.text) # added for debugging
        return None, ex


def get_temp(weather_data):
    try:
        temp = weather_data['main']['temp']
        return temp
    except KeyError:
        print('This data is not in the expected format')
        return 'Unknown'


if __name__ == '__main__':
    main()
