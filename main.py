"""
POKEMON MASTER
Game by Marcel Ruzicka
april-2020, ruzicka_marcel@yahoo.com
"""

from trainer import Trainer
from pokemon import Pokemon

# Pokemons:
"""Grass Pokemons; 110 health, normal damage"""
bulbasaur = Pokemon("Bulbasaur", 1, "Grass", 110)
ivysaur = Pokemon("Ivysaur", 1, "Grass", 110)
venusaur = Pokemon("Venusaur", 1, "Grass", 110)

"""Fire Pokemons; 100 health, 30 % more damage"""
charmander = Pokemon("Charmander", 1, "Fire", 100)
charmeleon = Pokemon("Charmeleon", 1, "Fire", 100)
charizard = Pokemon("Charizard", 1, "Fire", 100)

"""Water Pokemons; 100 health, 15 % more damage"""
squirtle = Pokemon("Squirtle", 1, "Water", 100)
wartortle = Pokemon("Wartortle", 1, "Water", 100)
blastoise = Pokemon("Blastoise", 1, "Water", 100)

"""Bug Pokemons; 100 health, normal damage"""
caterpie = Pokemon("Caterpie", 1, "Bug", 100)
metapod = Pokemon("Metapod", 1, "Bug", 100)
butterfree = Pokemon("Butterfree", 1, "Bug", 100)

"""Flying Pokemons; 100 health, 15 % more damage"""
pidgey = Pokemon("Pidgey", 1, "Flying", 100)
pidgeotto = Pokemon("Pidgeotto", 1, "Flying", 100)
pidgeot = Pokemon("Pidgeot", 1, "Flying", 100)

"""Normal Pokemons; 130 health, 40 % less damage"""
rattata = Pokemon("Rattata", 1, "Normal", 130)
raticate = Pokemon("Raticate", 1, "Normal", 130)
meowth = Pokemon("Meowth", 1, "Normal", 130)

"""Poison Pokemons; 100 health, 30 % more damage"""
ekans = Pokemon("Ekans", 1, "Poison", 100)
arbok = Pokemon("Arbok", 1, "Poison", 100)
nidoran = Pokemon("Nidoran", 1, "Poison", 100)

"""Electric Pokemons; 90 health, 30 % more damage"""
pikachu = Pokemon("Pikachu", 1, "Electric", 90)
raichu = Pokemon("Raichu", 1, "Electric", 90)
jolteon = Pokemon("Jolteon", 1, "Electric", 90)

"""Ground Pokemons; 100 health, 20 % more damage"""
sandshrew = Pokemon("Sandshrew", 1, "Ground", 100)
sandslash = Pokemon("Sandslash", 1, "Ground", 100)
diglett = Pokemon("Diglett", 1, "Ground", 100)

"""Fighting Pokemnos; 160 health, 20 % less damage"""
mankey = Pokemon("Mankey", 1, "Fighting", 160)
primeape = Pokemon("Primeape", 1, "Fighting", 160)
machoke = Pokemon("Machoke", 1, "Fighting", 160)

######################
##### Instances  #####
######################

#marcel = Trainer("Marcel", [squirtle, machoke, primeape, charmander, sandshrew, sandslash, raichu])
marcel = Trainer("Marcel", [machoke, sandshrew, sandslash, arbok, ekans, meowth, mankey])
print(marcel)

jakub = Trainer("Jakub", [raticate, venusaur, squirtle, blastoise, mankey, caterpie, diglett])
print(jakub)

######################
##### Play below #####
######################

marcel.activate_warrior()
jakub.activate_warrior()

marcel.attack_trainer(jakub)
jakub.attack_trainer(marcel)
marcel.attack_trainer(jakub)
jakub.attack_trainer(marcel)
marcel.attack_trainer(jakub)
jakub.attack_trainer(marcel)
marcel.attack_trainer(jakub)
jakub.attack_trainer(marcel)
marcel.attack_trainer(jakub)
jakub.attack_trainer(marcel)
marcel.attack_trainer(jakub)
jakub.attack_trainer(marcel)
print(marcel.active.current_health)
print(jakub.active.current_health)