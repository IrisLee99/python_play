import requests

city = 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=2d2f25fe57a14ccbbd9151141262210&q={}'.format(city)

response = requests.get(url)

weather_json = response.json()
temp = weather_json['current']['temp_c']
description = weather_json['current']['condition']['text']

print('Today\'s weather in {}: {}, {}°C'.format(city, description, temp))