from django.shortcuts import render
from django.shortcuts import get_list_or_404
from pokemon.models import Pokemon
import csv


def main(request):

    objects = Pokemon.objects.all()

    return render(request, 'pokemon/main.html', {'pokemon': objects})

def wiki_page(request, entry):
    
    pokemon = get_list_or_404(Pokemon, entry=entry)

    return render(request, 'pokemon/wiki-page.html', {'pokemon': pokemon})