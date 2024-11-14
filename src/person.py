class Person:

    def __init__(self):
        self.__live = 10
        self.is_dead = False

    def get_hp(self):
        return self.__live

    def attack(self, defender):
        if defender.__live > 0:
            defender.__live -= 1
        else:
            defender.is_dead = True
 
    def check_if_dead(self):
        return self.is_dead

    def resurect(self):
        self.__live = 10
        self.is_dead = False
