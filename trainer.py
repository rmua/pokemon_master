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
    self.active = None
    
  def __repr__(self):
    return "{} have chosen theese warriors: \n{}\n".format(self.name, self.characters_names)
    
  def team_health(self):
    self.team_health = self.characters.get_current_health()
    
  def activate_warrior(self):
    print("Activate a warrior from your list, {}! \n".format(self.name))
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
    if self.name == opponent.name:
      print("Trainer {} can not battle himself!".format(self.name))
      return
    elif self.name != opponent.name:
      self.active.attack(opponent.active)
      print("Trainer {} brought it on trainer {}.\n".format(self.name, opponent.name))
      return