class Person:

    __live = 10

    def get_hp(self):
        return self.__live

    def attack(self, defender):
        defender.__live -= 1
