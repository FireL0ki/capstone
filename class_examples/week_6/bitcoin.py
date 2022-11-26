import requests
from pprint import pprint


def main():
    bitcoin = get_user_input()
    dollar_exchange_rate = exchange_rate_dollars()
    bitcoin_value_in_dollars = convert_bitcoin_to_dollars(bitcoin, dollar_exchange_rate)
    display_result(bitcoin, bitcoin_value_in_dollars)


def get_user_input():
    bitcoin = float(input('Enter the number of bitcoin: '))
    return bitcoin


def exchange_rate_dollars():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = response.json()

    exchange_rate_dollars = data['bpi']['USD']['rate_float']
    return exchange_rate_dollars


def convert_bitcoin_to_dollars(bitcoin, dollar_exchange_rate):
    bitcoin_value_in_dollars = bitcoin * dollar_exchange_rate
    return bitcoin_value_in_dollars


def display_result(bitcoin, bitcoin_value_in_dollars):
    print(f'{bitcoin} Bitcoin is equivalent to ${bitcoin_value_in_dollars}')


if __name__ == '__main__':
    main()