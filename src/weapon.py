class Weapon:
    def __init__(self, damage):
        self.damage = damage

    def use(self, target):
        target.take_damage(self.damage)


class Knife(Weapon):
    def __init__(self):
        super().__init__(damage=2)


class Gun(Weapon):
    def __init__(self):
        super().__init__(damage=5)
