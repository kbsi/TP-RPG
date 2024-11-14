from .weapon import Weapon


class Person:
    __armor_power = 1
    __initial_hp = 10

    def __init__(self, with_armor=False):
        self.live = Person.__initial_hp
        self.is_dead = False
        self.armor = with_armor

    def get_hp(self):
        return self.live

    def attack(self, defender, weapon=None):
        damage = weapon.damage if weapon else 1

        if defender.armor:
            damage -= Person.__armor_power

        if defender.live > 0:
            defender.live -= damage

            if defender.live <= 0:
                defender.is_dead = True
                defender.live = 0

    def check_if_dead(self):
        return self.is_dead

    def resurect(self):
        self.live = Person.__initial_hp
        self.is_dead = False
