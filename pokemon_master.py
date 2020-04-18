"""
Pokemon Game - backup of original script
Author: Marcel Ruzicka, ruzicka_marcel@yahoo.com, april-2020
"""

import random


class Pokemon:
  def __init__(self, name, level, type_of, max_health, current_health, knocked_out):
    self.name = name
    self.level = level
    self.type_of = type_of
    self.max_health = max_health
    self.current_health = current_health
    self.hidden_points = 0
    if knocked_out == True:
      self.knocked_out = True
    else:
      self.knocked_out = False
      
  def __repr__(self):
    return "Pokemon {}, with current health {}, level {}".format(self.name.upper(), self.current_health, self.level)  
    
  def attack(self, other):
    self.other = other
    points = random.randint(1, 81)
    if self.name == self.other.name:
      print("{} can not battle himself!".format(self.name))
      return
    if self.type_of == "Fire" or "Poison" or "Electric":
      points = points * 1.3
    if self.type_of == "Ground":
      points = points * 1.2
    if self.type_of == "Water" or "Flying":
      points = points * 1.15
    if self.type_of == "Fighting":
      points = points * 0.8
    if self.type_of == "Normal":
      points = points * 0.6
    if points > self.other.current_health:
      points = self.other.current_health
    if self.knocked_out == True:
      print("{} can not attack, because he is allready KO!\n".format(self.name))
      return
    elif self.other.knocked_out == True:
      print("{name} can not gain health from {other}, because {other} is allready KO!\n".format(name = self.name, other = other.name))
      return
    
    self.current_health += points
    
    if self.current_health > self.max_health:
      self.hidden_points += (self.current_health - self.max_health)
      if self.hidden_points > self.other.current_health:
        self.hidden_points += self.other.current_health
      self.current_health = self.max_health
      
    self.level_up(self.hidden_points)
    self.other.lose_health(points)
    #print("Level: " + str(self.level))
    #print("Hidden points: " + str(self.hidden_points))
    print("{name} has attacked {other} with {type} and got {points} points from him. {name}'s current health is {current_health}.\n".format(name = self.name, other = other.name, type = self.type_of.lower(), points = str(points), current_health = self.current_health))
  
  def lose_health(self, points):
    self.current_health = self.current_health - points
    if self.current_health <= 0:
      self.knocked_out = True
      self.level = 1
      print("{} has been knocked out!\n".format(self.name))
    return self.current_health
    
  def level_up(self, hidden_points):
    if self.hidden_points >= 100:
      self.level += 1
      self.hidden_points = 0
      self.max_health = self.max_health + 100
      print("{} grew up to level {}.".format(self.name, self.level))
    return self.max_health, self.level

class Trainer:
  def __init__(self, name, characters):
    self.name = name
    self.characters = characters
    if len(self.characters) > 6:
      self.characters = self.characters[0:6]
      
    self.potion = ["strawberry", "bananna", "chocolatte", "cranberry", "apple", "mango"]
    
  def __repr__(self):
    return "{} have chosen theese warriors: \n{}\n".format(self.name, self.characters)
    
  def activate_warrior(self, warrior):
    self.active = warrior
    self.break_ = False
    if self.active.name in self.characters:
      print("{} is now active for trainer {}\n".format(self.active.name.upper(), self.name.upper()))
      return
    else:
      print("You can not activate a warrior from outside your list!")
      self.break_ = True 
    return
    
  def attack_trainer(self, opponent):
    self.opponent = opponent
    
    pokemon = Pokemon(self.active.name, self.active.level, self.active.type_of, self.active.max_health, self.active.current_health, self.active.knocked_out)
    opponents_pokemon = Pokemon(self.opponent.active.name, self.opponent.active.level, self.opponent.active.type_of, self.opponent.active.max_health, self.opponent.active.current_health, self.opponent.active.knocked_out)
    
    if self.name == self.opponent.name:
      self.break_ = True
      print("Trainer {} can not battle himself!".format(self.name))
      return
    
    if self.break_ != True:
      pokemon.attack(opponents_pokemon)
      print("Trainer {} brought it on trainer {}.\n".format(self.name, self.opponent.name))
      return    

      
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


marcel = Trainer("Marcel", [squirtle.name, machoke.name, primeape.name, charmander.name, sandshrew.name, sandslash.name, raichu.name])
#print(marcel)

jakub = Trainer("Jakub", [raticate.name, venusaur.name, squirtle.name, blastoise.name, mankey.name, caterpie.name, diglett.name])
#print(jakub)

marcel.activate_warrior(squirtle)
jakub.activate_warrior(caterpie)

marcel.attack_trainer(jakub)
jakub.attack_trainer(marcel)

#primeape.attack(caterpie)
#caterpie.attack(primeape)











      
      