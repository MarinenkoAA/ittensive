import requests
import json
r = requests.get("https://geocode-maps.yandex.ru/1.x/?apikey=3f355b88-81e9-4bbf-a0a4-eb687fdea256&geocode=Самара&format=json&results=1")
answer = json.loads (r.content)
print(answer['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[0])