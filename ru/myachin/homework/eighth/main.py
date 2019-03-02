# ### Задача 1 (2 балла)
# С помощью [API World Bank](https://datahelpdesk.worldbank.org/knowledgebase/articles/898590-api-country-queries),
# напишите функцию `get_capital(country_code)`, принимающую на вход ISO 3166-1 код государства и возвращающую название
# его столицы (в том виде, в котором оно возвращается этим API). Если вы хотите, чтобы API использовало формат JSON,
# укажите словарь `{'format':'json'}` в качестве второго аргумента `requests.get`. (Вы можете использовать как JSON,
# так и XML-интерфейс, на ваш выбор.) Обратите внимание: код страны здесь надо передавать как часть URL.

import requests


def get_capital(country_code):
    r = requests.get("http://api.worldbank.org/v2/countries/" + country_code, {'format': 'json'})
    data = r.json()
    return data[1][0]['capitalCity']


# ### Задача 2 (2 балла)
# Написать функцию `diff_lat(place1, place2)`, которая бы с помощью
# [геокодера Яндекса](https://tech.yandex.ru/maps/doc/geocoder/desc/concepts/input_params-docpage/) находила
# координаты двух объектов, заданных строками `place1` и `place2`, и возвращала бы число с плавающей точкой,
# являющееся ответом на вопрос: на сколько градусов `place2` севернее, по сравнению с `place1`?

def diff_lat(place1, place2):
    geo_url = "https://geocode-maps.yandex.ru/1.x/"
    r = requests.get(geo_url, params={'geocode': place1, 'format': 'json'})
    r2 = requests.get(geo_url, params={'geocode': place2, 'format': 'json'})

    data_1 = r.json()
    data_2 = r2.json()
    lat_1 = data_1['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[1]
    lat_2 = data_2['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[1]

    return float(lat_2) - float(lat_1)


# ### Задача 3 (2 балла)
# На сайте https://dronestre.am собираются данные об ударах дронов США. У него есть простое API, позволяющее получить
# информацию о каждом ударе в виде JSON-файла. Адрес для API: https://api.dronestre.am/data
# Написать функцию `strikes_per_country(year)`, принимающую на вход год в виде целого числа (например, `2015`) и
# возвращающую словарь, ключами которого являются страны, а значениями — число ударов в этой стране.
# 
# **Подсказка 1.** API не принимает параметр *year* (и вообще никаких параметров не принимает). Вам придётся скачать
# все данные и вытащить из них только те записи, которые вам нужны. Дата в данных указана в виде строки в стандартном
# формате. Можно проверить, что строка начинается с некоторого префикса с помощью `.startswith`.
# Например, `"Hello".startswith("He")` возвращает `True`.
# 
# **Подсказка 2.** Попробуйте использовать `collections.Counter` (`from collections import Counter`). Почитайте в
# документации, что он делает.
# 
# **Подсказка 3.** Для ускорения работы функции вы можете записать код, который будет запрашивать информацию с сайта,
# до описания функции:
# 
#     # (make request)
#     # json_data = (some lines to get data)
#     def strikes_per_country(year):
#         # query json_data for data you need

from collections import Counter

r = requests.get("http://api.dronestre.am/data", {'format': 'json'})
strikes = r.json()['strike']


def strikes_per_country(year):
    c = Counter()
    for strike in strikes:
        if strike['date'].startswith(str(year)):
            c[strike['country']] += 1

    return dict(c)


# ### Задача 4 (3 балла)
# 
# С помощью [API Google Books](https://developers.google.com/books/docs/v1/getting_started) можно получать информацию
# о различных книгах. Например, вот так можно получить данные по книге по её
# ISBN: https://www.googleapis.com/books/v1/volumes?q=isbn:9785699648146. Напишите функцию `book_table(isbns)`,
# принимающую на вход список ISBN'ов и возвращающую таблицу pandas, содержащую заглавие, авторов, язык и число страниц.
# Названия колонок должны соответствовать названиям полей в ответе API. Если авторов несколько, они должны быть
# разделены запятой и пробелом. Пример см. в тесте.

import pandas as pd


def book_table(isbns):
    url = 'https://www.googleapis.com/books/v1/volumes'
    df = pd.DataFrame(columns=['title', 'authors', 'language', 'pageCount'])
    for i in range(0, len(isbns)):
        isbn = isbns[i]
        r = requests.get(url, params={'q': 'isbn:' + isbn})
        data = r.json()
        items = data['items'][0]['volumeInfo']
        title = items['title']
        authors = items['authors']
        language = items['language']
        page_count = items['pageCount']
        series = pd.Series([title, ", ".join(authors), language, page_count],
                           index=['title', 'authors', 'language', 'pageCount'])
        df.loc[i] = series

    return df


# ### Задача 5 (1 балл)
# Написать функцию `float_or_nan`, которая преобразует вещественное число, записанное в строке, в формат `float`.
# При этом если в строке записано что-то, что не может быть преобразовано во `float`, должно быть возвращено специальное
# значение `float("nan")`.
# 
# **Подсказка:** вам предстоит использовать конструкцию `try/except` для решения этой задачи.

def float_or_nan(value):
    try:
        return float(value)
    except ValueError:
        return float("nan")


# ### Задача 6 (1 балл)
# Написать функцию `find(some_list, element)`, которая возвращает индекс первого элемента в списке `some_list`,
# равного `element`. Если такого элемента нет, должно быть возвращено `-1`. Использовать циклы запрещено.
# 
# **Подсказка.** У списков есть метод `index`, который делает ровно то, что нужно, за одним исключением: если элемент
# не найден, происходит исключение (exception) `ValueError`. Здесь и в следующих двух задачах вам необходимо
# использовать конструкцию `try/catch`, чтобы обработать исключение. Подробнее про исключения можно прочитать
# [здесь](http://python.math-hse.info:8080/github/ischurov/pythonhse/blob/master/Lecture%208.ipynb#Немного-про-исключения).

def find(some_list, element):
    try:
        return some_list.index(element)
    except ValueError:
        return -1


# ### Задача 7 (2 балла)
#
# Напишите функцию `power_or_nan(a, b)`, которая возводит вещественное положительное число `a` в степень, заданную
# вещественным положителным числом `b`, и возвращает результат. Если числа оказались слишком большими и в процессе
# вычисления произошло переполнение, функция должна вернуть специальное значение `float("NaN")`.
#
# **Примечание.** Python 3 может работать со сколь угодно большими целыми числами (в принципе помещающимися в память),
# но для чисел с плавающей точкой существует ограничение: слишком большие числа просто невозможно записать.
# Если вы работаете с целыми числами и в какой-то момент эти числа становятся очень-очень большими, то компьютер будет
# очень долго думать: например, попробуйте вычислить `9 ** (9 ** 9)` (прекратить вычисление можно с
# помощью *Kernel → Interrupt*). Если аналогичное вычисление выполнить с числами с плавающей точкой, возникнет
# переполнение (попробуйте). В данной задаче требуется работать только с числами с плавающей точкой. Если вы хотите
# записать целое число как число с плавающей точкой, это можно сделать, поставив точку: например,
# `type(9)` — это `int`, а `type(9.)` — это `float`. Чтобы преобразовать переменную к типа `float` нужно использовать
# одноимённую функцию (например: `y = float(x)`).

def power_or_nan(a, b):
    try:
        return float(a) ** float(b)
    except OverflowError:
        return float("nan")
