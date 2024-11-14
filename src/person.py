from .weapon import Weapon

class Person:

    def __init__(self):
        self.__live = 10
        self.is_dead = False

    def get_hp(self):
        return self.__live

    def attack(self, defender, weapon: Weapon):
        defender.__live -= weapon.damage
        if defender.__live <= 0:
            defender.is_dead = True
            defender.__live = 0
        else:
            defender.is_dead = True
 
    def check_if_dead(self):
        return self.is_dead

    def resurect(self):
        self.__live = 10
        self.is_dead = False
