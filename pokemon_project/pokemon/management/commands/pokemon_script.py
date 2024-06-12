from django.core.management.base import BaseCommand
from pokemon.models import Pokemon
import csv
import json


class Command(BaseCommand):
    help = 'Import data from the information csv file to the project'

    def handle(self, *args, **kwargs):

        csv_file = 'D:/Django/pokemon_project/info/final_all_info.csv'



        with open(csv_file, encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)
            type_effects = []
            for row in reader:


                images = row['images']
                image_list = images.split(', ')

                # Append all the elements corresponding with their type effectiveness
                keys = list(row.keys())
                type_effects.append({row[keys[1]]: [{'4x': []}, {'2x': []}, {'1x': []}, {'0.5x': []}, {'0x': []}]})

                for i in range(12, 30):
                    if row[keys[i]] == '4':
                        type_effects[int(row['entry'])-1][row['name']][0]['4x'].append(keys[i])
                    if row[keys[i]] == '2':
                        type_effects[int(row['entry'])-1][row['name']][1]['2x'].append(keys[i])
                    if row[keys[i]] == '1':
                        type_effects[int(row['entry'])-1][row['name']][2]['1x'].append(keys[i])
                    if row[keys[i]] == '½':
                        type_effects[int(row['entry'])-1][row['name']][3]['0.5x'].append(keys[i])
                    if row[keys[i]] == '0':
                        type_effects[int(row['entry'])-1][row['name']][4]['0x'].append(keys[i])

                fourx = type_effects[int(row['entry'])-1][row['name']][0]['4x']
                twox = type_effects[int(row['entry'])-1][row['name']][1]['2x']
                onex = type_effects[int(row['entry'])-1][row['name']][2]['1x']
                halfx = type_effects[int(row['entry'])-1][row['name']][3]['0.5x']
                zerox = type_effects[int(row['entry'])-1][row['name']][4]['0x']
                # Initialize the pokemon
                pokemon = Pokemon(
                    # Data
                    entry=row['entry'],
                    name=row['name'],
                    type1=row['type1'],
                    type2=row['type2'],
                    sprite=row['sprite'],
                    images=image_list,

                    # Stats
                    hp=row['health'],
                    attack=row['attack'],
                    defense=row['defense'],
                    spattack=row['spattack'],
                    spdefense=row['spdefense'],
                    speed=row['speed'],
                    total=row['total'],
                    
                    # Type effectiveness
                    fourx=fourx,
                    twox=twox,
                    onex=onex,
                    halfx=halfx,
                    zerox=zerox,
                )
                pokemon.save()
                self.stdout.write(self.style.SUCCESS(f"Successfully imported {pokemon.name}"))