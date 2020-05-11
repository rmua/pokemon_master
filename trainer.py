"""
Script for the Pokemon Master game
Author: Marcel Ruzicka
may-2020, ruzicka_marcel@yahoo.com
"""

from pokemon import Pokemon

class Trainer:
  def __init__(self, name, characters):
    self.name = name
    self.characters = characters
    if len(self.characters) > 6:
      self.characters = self.characters[0:6]
    self.characters_names = ""
    for character in self.characters:
      self.characters_names += character.name + "\n"
    #self.characters_names = [character.name for character in self.characters]
    self.active = None
    self.team_health = sum([character.current_health for character in self.characters])
    
  def __repr__(self):
    return "{} have chosen theese warriors: \n{}\n".format(self.name, self.characters_names)
    
  def team_health(self):
    self.team_health = 0
    self.team_health += [character.current_health for character in self.characters]
    return self.team_health
    
  def team_list(self):
    for warrior in self.characters:
      if warrior.knocked_out:
        self.characters.remove(warrior)
    self.characters_names = ""
    for character in self.characters:
      self.characters_names += character.name + "\n"
    return self.characters, self.characters_names
    
  def activate_warrior(self):
    print("{}, activate a warrior from your list: \n{}".format(self.name, self.characters_names))
    while self.active == None:
      user_input = input("Type the name: ")
      for warrior in self.characters:
        if warrior.name == user_input:
          self.active = warrior
          print("{} is now active for trainer {}\n".format(self.active.name.upper(), self.name.upper()))
          break
      else:
        print("You must activate a warrior from your list. Try again! \n")

          
  def attack_trainer(self, opponent):
    if self.active.current_health > 0:      
      if self.name == opponent.name:
        print("Trainer {} can not battle himself!".format(self.name))
        return
      elif self.name != opponent.name:
        self.active.attack(opponent.active)
        #opponent.team_health()
    else: 
      print("{} is KO".format(self.active.name))
      self.team_list() # update the team list
      self.active = None
      if self.characters:
        self.activate_warrior()
      else:
        return


      