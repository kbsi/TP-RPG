from src.person import Person
from src.weapon import Gun, Knife
import random


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round = 1
        self.history = []

    def start(self, rounds=20) -> Person:
        weapons = [Gun(), Knife(), None]

        while self.player1.get_hp() >= 0 and self.player2.get_hp() >= 0 and self.round <= rounds:
            weapon = random.choice(weapons)

            self.history.append(f'** Round {self.round} **')

            self.player1.attack(self.player2, weapon)
            self.player2.attack(self.player1, weapon)

            self.history.append(f'Player 1 HP: {self.player1.get_hp()}')
            self.history.append(f'Player 2 HP: {self.player2.get_hp()}')
            self.history.append('')

            self.round += 1

        if self.player1.get_hp() > self.player2.get_hp():
            return self.player1
        elif self.player1.get_hp() < self.player2.get_hp():
            return self.player2
        else:
            return None

    def get_history(self):
        return self.history
