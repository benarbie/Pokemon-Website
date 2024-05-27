from django.shortcuts import render
import csv


def pokemon(request):

    data = []

    with open('../info/mons.csv') as file:
        reader = csv.reader(file)
        for mon in reader:
            data.append({'name': mon[0], 'type1': mon[1], 'type2': mon[2], 'src': mon[3]})


    return render(request, 'pokemon/main.html', {'data': data})
