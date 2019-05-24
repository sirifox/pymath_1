# Задание 1
# Дан список вида:
# Напишите функцию, которая возвращает сумму элементов на диагонали. Т. е. 13+32+23+35.

data = [
[13, 25, 23, 34],
[45, 32, 44, 47],
[12, 33, 23, 95],
[13, 53, 34, 35],
]

def list_sum(data):
  res = 0
  for num, lis in enumerate(data):
      res += lis[num]
  return res

print(list_sum(data))

# Задание 2
# Дан список чисел, часть из которых имеют строковый тип или содержат буквы. Напишите функцию, которая возвращает сумму квадратов элементов, которые могут быть числами.

data = [1, '5', 'abc', 20, '2']

def list_sum(data):
  res = 0
  for elem in data:
      try:
        res += float(elem) ** 2
      except:
        pass
  return res

print(list_sum(data))

# Задание 3
# Напишите функцию, которая возвращает название валюты (поле ‘Name') с максимальным значением курса с помощью сервиса https://www.cbr-xml-daily.ru/daily_json.js

import requests


def req_cbr(URL):
  resp = requests.get(URL).json()
  max_val = 0.0
  for key in resp['Valute'].keys():
    if max_val < resp['Valute'][key]['Value'] / resp['Valute'][key]['Nominal']:
      max_val = resp['Valute'][key]['Value'] / resp['Valute'][key]['Nominal']
      res = key
  return res


print(req_cbr('https://www.cbr-xml-daily.ru/daily_json.js'))

# Задание 5
# Напишите функцию, возвращающую сумму первых n чисел Фибоначчи
# это ряд чисел, в котором каждое следующее число равно сумме двух предыдущих

def fib_sum(val):
  try:
    val = int(val) - 1
    fib_list = [1]
    for elem in range(val):
      if elem == 0:
        tmp = 0
      else:
        tmp = fib_list[elem-1]
      fib_list.append(fib_list[elem] + tmp)
    print(fib_list)
    return sum(fib_list)
  except ValueError:
    return 'Неверный формат ввода'

print(fib_sum(input('Сколько чисел Фибоначчи необходимо просуммировать? : ')))

# Задание 6
# Напишите функцию, преобразующую произвольный список вида [‘2018-01-01’, ‘yandex’, ‘cpc’, 100] в словарь {‘2018-01-01’: {‘yandex’: {‘cpc’: 100}}}

import pprint


def transform(t_list):
  t_dict = dict.fromkeys([t_list[len(t_list) - 2]], t_list[len(t_list) - 1])
  for i in range(3,len(t_list) + 1):
    t_dict = dict.fromkeys([t_list[len(t_list) - i]], t_dict)

  return(t_dict)

list1 = ['2018-01-01', 'yandex', 'cpc', 100]
pprint.pprint(transform(list1))
