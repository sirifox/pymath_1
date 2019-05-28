# Задание 1
# Напишите функцию date_range, которая возвращает список дней между датами start_date и end_date. Даты должны вводиться в формате YYYY-MM-DD.

# Задание 2
# Дополните функцию из первого задания проверкой на корректность дат. В случае неверного формата или если start_date > end_date должен возвращаться пустой список.

import datetime as dt


def date_range(start_date, end_date):
  try:
    start_date = dt.date(int(start_date.split('-')[0]), int(start_date.split('-')[1]), int(start_date.split('-')[2]))
    end_date = dt.date(int(end_date.split('-')[0]), int(end_date.split('-')[1]), int(end_date.split('-')[2]))
    if start_date > end_date:
      raise ValueError
    date_list=[]
    for n in range(int ((end_date - start_date).days)+1):
      date_list.append((start_date + dt.timedelta(days=n)).strftime("%Y-%m-%d"))

    return date_list
  except ValueError:
    return []

start_date = input('Введите начальную дату в формате YYYY-MM-DD: ')
end_date = input('Введите конечную дату в формате YYYY-MM-DD: ')
print(date_range(start_date, end_date))

# Задание 3
# Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
# stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]

# Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой даты возвращает True (дата корректна) или False (некорректная дата).

import datetime as dt


def stream_check(datestream):
  check_list =[]
  for date in datestream:    
    try:
      dt.date(int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2]))
      check_list.append(True)
    except:
      check_list.append(False)

  return check_list

stream = ['2018-04-02', '2018-02-29', '2018-19-02']
print(stream_check(stream))

# Задание 4
# Напишите функцию, которая возвращает список дат с 1 по вчерашний день текущего месяца. Если дан 1 день месяца, то возвращается список дней прошлого месяца.

import pprint
import datetime as dt


def date_listing():
  start_date = dt.datetime.today()-dt.timedelta(days=1)
  end_date = start_date.replace(day=1)
  # print (start_date, end_date)
  date_list = []
  for n in range(int ((start_date - end_date).days)+1):
    date_list.append((start_date - dt.timedelta(days=n)).strftime("%Y-%m-%d"))
  return date_list

pprint.pprint(date_listing())
