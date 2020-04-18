"""
Script for the Pokemon Master game
Author: Marcel Ruzicka
april-2020, ruzicka_marcel@yahoo.com
"""

from pokemon import Pokemon
import random

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