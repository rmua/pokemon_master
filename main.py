"""
POKEMON MASTER
Game by Marcel Ruzicka
april-2020, ruzicka_marcel@yahoo.com
"""

from trainer import Trainer
from pokemon import Pokemon

# Pokemons:
"""Grass Pokemons; 110 health, normal damage"""
bulbasaur = Pokemon("Bulbasaur", 1, "Grass", 110, 110, False)
ivysaur = Pokemon("Ivysaur", 1, "Grass", 110, 110, False)
venusaur = Pokemon("Venusaur", 1, "Grass", 110, 110, False)

"""Fire Pokemons; 100 health, 30 % more damage"""
charmander = Pokemon("Charmander", 1, "Fire", 100, 100, False)
charmeleon = Pokemon("Charmeleon", 1, "Fire", 100, 100, False)
charizard = Pokemon("Charizard", 1, "Fire", 100, 100, False)

"""Water Pokemons; 100 health, 15 % more damage"""
squirtle = Pokemon("Squirtle", 1, "Water", 100, 100, False)
wartortle = Pokemon("Wartortle", 1, "Water", 100, 100, False)
blastoise = Pokemon("Blastoise", 1, "Water", 100, 100, False)

"""Bug Pokemons; 100 health, normal damage"""
caterpie = Pokemon("Caterpie", 1, "Bug", 100, 100, False)
metapod = Pokemon("Metapod", 1, "Bug", 100, 100, False)
butterfree = Pokemon("Butterfree", 1, "Bug", 100, 100, False)

"""Flying Pokemons; 100 health, 15 % more damage"""
pidgey = Pokemon("Pidgey", 1, "Flying", 100, 100, False)
pidgeotto = Pokemon("Pidgeotto", 1, "Flying", 100, 100, False)
pidgeot = Pokemon("Pidgeot", 1, "Flying", 100, 100, False)

"""Normal Pokemons; 130 health, 40 % less damage"""
rattata = Pokemon("Rattata", 1, "Normal", 130, 130, False)
raticate = Pokemon("Raticate", 1, "Normal", 130, 130, False)
meowth = Pokemon("Meowth", 1, "Normal", 130, 130, False)

"""Poison Pokemons; 100 health, 30 % more damage"""
ekans = Pokemon("Ekans", 1, "Poison", 100, 100, False)
arbok = Pokemon("Arbok", 1, "Poison", 100, 100, False)
nidoran = Pokemon("Nidoran", 1, "Poison", 100, 100, False)

"""Electric Pokemons; 90 health, 30 % more damage"""
pikachu = Pokemon("Pikachu", 1, "Electric", 90, 90, False)
raichu = Pokemon("Raichu", 1, "Electric", 90, 90, False)
jolteon = Pokemon("Jolteon", 1, "Electric", 90, 90, False)

"""Ground Pokemons; 100 health, 20 % more damage"""
sandshrew = Pokemon("Sandshrew", 1, "Ground", 100, 100, False)
sandslash = Pokemon("Sandslash", 1, "Ground", 100, 100, False)
diglett = Pokemon("Diglett", 1, "Ground", 100, 100, False)

"""Fighting Pokemnos; 160 health, 20 % less damage"""
mankey = Pokemon("Mankey", 1, "Fighting", 160, 160, False)
primeape = Pokemon("Primeape", 1, "Fighting", 160, 160, False)
machoke = Pokemon("Machoke", 1, "Fighting", 160, 160, False)

######################
##### Instances  #####
######################

marcel = Trainer("Marcel", [squirtle.name, machoke.name, primeape.name, charmander.name, sandshrew.name, sandslash.name, raichu.name])
#print(marcel)

jakub = Trainer("Jakub", [raticate.name, venusaur.name, squirtle.name, blastoise.name, mankey.name, caterpie.name, diglett.name])
#print(jakub)

######################
##### Play below #####
######################

marcel.activate_warrior(squirtle)
jakub.activate_warrior(caterpie)

marcel.attack_trainer(jakub)
