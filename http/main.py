import requests

response = requests.get('https://api.open-notify.org/astros.json')
data = response.json()
print(data)