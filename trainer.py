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
    self.characters_names = [character.name for character in self.characters]
    if len(self.characters) > 6:
      self.characters = self.characters[0:6]
      self.characters_names = self.characters_names[0:6]
    self.potion = ["strawberry", "bananna", "chocolatte", "cranberry", "apple", "mango"]
    
  def __repr__(self):
    return "{} have chosen theese warriors: \n{}\n".format(self.name, self.characters_names)
    
  def activate_warrior(self):
    print("Activate a warrior from your list, {}! \n".format(self.name))
    self.active = None
    while self.active == None:
      try:
        user_input = input("Type in a warrior: ")
        for warrior in self.characters:
          if warrior.name == user_input:
            self.active = warrior
            print("{} is now active for trainer {}\n".format(self.active.name.upper(), self.name.upper()))
            break
        else:
          print("You must activate a warrior from your list. Try again! \n")
      except NameError:
        print("Use quotation marks \"\" for inputs")

          
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