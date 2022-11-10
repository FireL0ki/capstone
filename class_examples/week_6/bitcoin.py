import requests
from pprint import pprint

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url)
data = response.json()
pprint(data)

exchange_rate_dollars = data['bpi']['USD']['rate_float']
print(exchange_rate_dollars)


bitcoin = float(input('Enter the number of bitcoin: '))

bitcoin_value_in_dollars = bitcoin * exchange_rate_dollars

print(f'{bitcoin} Bitcoin is equivalent to ${bitcoin_value_in_dollars}')

