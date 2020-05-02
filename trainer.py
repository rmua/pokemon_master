"""
Script for the Pokemon Master game
Author: Marcel Ruzicka
may-2020, ruzicka_marcel@yahoo.com
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
    self.active = None
    
  def __repr__(self):
    return "{} have chosen theese warriors: \n{}\n".format(self.name, self.characters_names)
    
  def team_health(self):
    self.team_health = self.characters.get_current_health()
    return self.team_health
    
  def team_list(self):
    for warrior in self.characters:
      if warrior.knocked_out:
        self.characters.remove(warrior)
    self.characters_names = [character.name for character in self.characters]
    return self.characters, self.characters_names
    
  def activate_warrior(self):
    print("{}, activate a warrior from your list: {}".format(self.name, self.characters_names))
    while self.active == None:
      #try: use with the except conditions below the block in Python2
      user_input = input("Type the name: ")
      for warrior in self.characters:
        if warrior.name == user_input:
          self.active = warrior
          print("{} is now active for trainer {}\n".format(self.active.name.upper(), self.name.upper()))
          break
      else:
        print("You must activate a warrior from your list. Try again! \n")
      #except NameError:
        #print("Use quotation marks \"\" for inputs")
          
  def attack_trainer(self, opponent):
    #while len(opponent.characters) > 0 and len(self.characters) > 0:
    if self.active.current_health > 0:      
      if self.name == opponent.name:
        print("Trainer {} can not battle himself!".format(self.name))
        return
      elif self.name != opponent.name:
        self.active.attack(opponent.active)
        print("Trainer {} has attacked trainer {}.\n".format(self.name, opponent.name))
    else:
      print("{} is KO".format(self.active.name))
      self.team_list() # update the team list
      self.active = None
      return self.activate_warrior()

#    if len(opponent.characters) == 0:
#      print("Trainer {} wins the game!\n".format(self.name))
#      print("GAME OVER")
#    elif len(self.characters) == 0:
#      print("Trainer {} wins the game!\n".format(opponent.name))
#      print("GAME OVER")
      