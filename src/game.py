from src.person import Person


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round = 0

    def start(self, rounds=20) -> Person:
        while self.player1.get_hp() >= 0 and self.player2.get_hp() >= 0 and self.round < rounds:
            self.player1.attack(self.player2)
            self.player2.attack(self.player1)
            self.round += 1
            print(f'** Round {self.round} **')
            print(f'Player 1 HP: {self.player1.get_hp()}')
            print(f'Player 2 HP: {self.player2.get_hp()}')
            print('')

        if self.player1.get_hp() > self.player2.get_hp():
            return self.player1
        elif self.player1.get_hp() < self.player2.get_hp():
            return self.player2
        else:
            return None
