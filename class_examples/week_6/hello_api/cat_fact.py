import requests

try:
    response = requests.get('http://catfact.ninja/fact')
    print(response.status_code)

    response.raise_for_status()  #raise an exception for 400 or 500 code

    print(response.text)
    print(response.json())

    data = response.json()
    fact = data['fact']
    print(f'Here is a random cat fact: {fact}')

except Exception as e:
    print(e)
    print('There was an error making the request')