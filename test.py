import requests
json_data  = {"query":"Москва, Шаболовка, 37","limit":5,"fromBound":"CITY"}
resp = requests.post('https://www.pochta.ru/suggestions/v2/suggestion.find-addresses', json=json_data)
resp.json()
print(resp.json()[0]['postalCode'])