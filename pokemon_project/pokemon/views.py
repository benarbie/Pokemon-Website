from django.shortcuts import render
import csv


def main(request):

    data = []

    with open('../info/mons.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for mon in reader:
            data.append({'name': mon[0], 'type1': mon[1], 'type2': mon[2], 'src': mon[3]})


    return render(request, 'pokemon/main.html', {'data': data})

def wiki_page(request):
    return render(request, 'pokemon/wiki-page.html')
