import unittest
from src.person import Person
from src.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Person(with_armor=True)
        self.player2 = Person()
        self.game = Game(self.player1, self.player2)


if __name__ == '__main__':
    unittest.main()
