import csv
from statistics import mode

with open('lesson4/data-398-2017-09-14.csv', 'r', encoding='windows 1251') as csv_stop:
    reader = csv.reader(csv_stop)
    headers = next(reader)
    headers = headers[0].split(';')
    reader = csv.DictReader(csv_stop, headers, delimiter=';')
    count = 0
    list_of_streets = []
    for row in reader:
        list_of_streets.append(row['"Street"'])
    print(mode(list_of_streets))
