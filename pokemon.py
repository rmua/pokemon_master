"""
Script for the Pokemon Master game
Author: Marcel Ruzicka
april-2020, ruzicka_marcel@yahoo.com
"""

import random

class Pokemon:
  def __init__(self, name, type_of, max_health):
    self.name = name
    self.level = 1
    self.type_of = type_of
    self.max_health = max_health
    self.current_health = max_health
    self.hidden_points = 0
    self.knocked_out = False
      
  def __repr__(self):
    return "Pokemon {}, with health {}, level {}".format(self.name.upper(), self.current_health, self.level)
    
  def attack(self, other):
    self.other = other
    points = random.randint(1, 61)
    #if self.name == self.other.name:
      #print("{} can not battle himself!".format(self.name))
      #return
    # conditions for attack based on type of pokemon:
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
    # checking if the pokemons are able to attack or to be attacked
    if self.knocked_out == True:
      print("{} can not attack, because he is allready KO!\n".format(self.name))
      return
    elif other.knocked_out == True:
      print("{name} can not gain health from {other}, because {other} is allready KO!\n".format(name = self.name, other = other.name))
      return
    self.current_health += points
    # formula for gaining hidden points to grew in level:
    if self.current_health > self.max_health:
      self.hidden_points += (self.current_health - self.max_health)
      if self.hidden_points > self.other.current_health:
        self.hidden_points += self.other.current_health
      self.current_health = self.max_health
    print("{} has attacked {} with {} and got {:3.0f} points from him. {}'s current health is {:3.0f}.\n".format(self.name, other.name, self.type_of.lower(), points, self.name, self.current_health))
    self.other.lose_health(points)
    self.level_up(self.hidden_points)
  
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
      print("{} grew up to level {}\n.".format(self.name, self.level))
    return self.max_health, self.level
    
  def get_current_health(self):
    return self.current_health