import zipfile

archive = zipfile.ZipFile('C:\\Users\\User\\Downloads\\otchet_ob_ispolnenii_kbrf_za_2017_god.zip', 'r')
print(archive.filelist)
print(archive.filelist[0].filename)
xls_file = archive.open(archive.filelist[0].filename)

import pandas as pd

df = pd.read_excel(xls_file, sheet_name=None, header=10)
xls_file.close()
print(df.keys())
budget = df['Доходы']['Федеральный бюджет']
print(budget)
handled_budget = budget.str.replace(",", ".").str.replace(" ", "").astype(float).fillna(budget)
print(handled_budget)

# handle exceptions
x = "hlkjlk"
x_number = None
try:
    x_number = float(x)
except ValueError:
    print("x is not a float number")

print("x_number = ", x_number)

x = "0"
x_number = None
try:
    x_number = float(x)
    print(1 / x_number)
except ZeroDivisionError as e:
    print(e)
finally:
    print("Cleared")
print("That's all")

# Use yandex geocoder API
import requests

r = requests.get("https://geocode-maps.yandex.ru/1.x/", params={'geocode': 'Шаболовка, 26c4'})
print(r.url)
print(r.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'xml')
for go in soup.find_all("GeoObject"):
    print(go.find("text").text)
    long, lat = go.find("Point").find("pos").text.split()
    print("longitude", long, "latitude", lat)

r = requests.get("https://geocode-maps.yandex.ru/1.x/", params={'geocode': 'Шаболовка, 26c4', 'format': 'json'})
data = r.json()
print(data.keys())
print(data['response'])
print(data['response']['GeoObjectCollection'].keys())
print(data['response']['GeoObjectCollection']['featureMember'])
print(data['response']['GeoObjectCollection']['featureMember'][0])
print(data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'])
