class Person:

    def __init__(self):
        self.__live = 10
        self.is_dead = False

    def get_hp(self):
        return self.__live

    def attack(self, defender):
        defender.__live -= 1
        defender.check_if_dead()

    def check_if_dead(self):
        if self.__live <= 0:
            self.__live = 0
            self.is_dead = True