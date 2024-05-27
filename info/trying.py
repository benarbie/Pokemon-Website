import csv


data = []

with open('mons.csv') as file:
    reader = csv.reader(file)
    for mon in reader:
        data.append({'name': mon[0], 'type1': mon[1], 'type2': mon[2]})

for item in data:
    print(item['type1'])

