"""
POKEMON MASTER
Game by Marcel Ruzicka
may-2020, ruzicka_marcel@yahoo.com
"""

from trainer import Trainer
from pokemon import Pokemon

# Pokemons:
"""Grass Pokemons; 110 health, normal damage"""
bulbasaur = Pokemon("Bulbasaur", "Grass", 110)
ivysaur = Pokemon("Ivysaur", "Grass", 110)
venusaur = Pokemon("Venusaur", "Grass", 110)

"""Fire Pokemons; 100 health, 30 % more damage"""
charmander = Pokemon("Charmander", "Fire", 100)
charmeleon = Pokemon("Charmeleon", "Fire", 100)
charizard = Pokemon("Charizard", "Fire", 100)

"""Water Pokemons; 100 health, 15 % more damage"""
squirtle = Pokemon("Squirtle", "Water", 100)
wartortle = Pokemon("Wartortle", "Water", 100)
blastoise = Pokemon("Blastoise", "Water", 100)

"""Bug Pokemons; 100 health, normal damage"""
caterpie = Pokemon("Caterpie", "Bug", 100)
metapod = Pokemon("Metapod", "Bug", 100)
butterfree = Pokemon("Butterfree", "Bug", 100)

"""Flying Pokemons; 100 health, 15 % more damage"""
pidgey = Pokemon("Pidgey", "Flying", 100)
pidgeotto = Pokemon("Pidgeotto", "Flying", 100)
pidgeot = Pokemon("Pidgeot", "Flying", 100)

"""Normal Pokemons; 130 health, 40 % less damage"""
rattata = Pokemon("Rattata", "Normal", 130)
raticate = Pokemon("Raticate", "Normal", 130)
meowth = Pokemon("Meowth", "Normal", 130)

"""Poison Pokemons; 100 health, 30 % more damage"""
ekans = Pokemon("Ekans", "Poison", 100)
arbok = Pokemon("Arbok", "Poison", 100)
nidoran = Pokemon("Nidoran", "Poison", 100)

"""Electric Pokemons; 90 health, 30 % more damage"""
pikachu = Pokemon("Pikachu", "Electric", 90)
raichu = Pokemon("Raichu", "Electric", 90)
jolteon = Pokemon("Jolteon", "Electric", 90)

"""Ground Pokemons; 100 health, 20 % more damage"""
sandshrew = Pokemon("Sandshrew", "Ground", 100)
sandslash = Pokemon("Sandslash", "Ground", 100)
diglett = Pokemon("Diglett", "Ground", 100)

"""Fighting Pokemnos; 160 health, 20 % less damage"""
mankey = Pokemon("Mankey", "Fighting", 160)
primeape = Pokemon("Primeape", "Fighting", 160)
machoke = Pokemon("Machoke", "Fighting", 160)

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