import unittest
from src.person import Person
from src.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Person(with_armor=True)
        self.player2 = Person()
        self.game = Game(self.player1, self.player2)

    def test_game_initialization(self):
        self.assertEqual(self.game.player1, self.player1)
        self.assertEqual(self.game.player2, self.player2)
        self.assertEqual(self.game.round, 1)

    def test_game_start(self):
        self.player1.live = 50
        self.player2.live = 0
        winner = self.game.start(rounds=1)
        self.assertIn(winner, [self.player1, self.player2])
        self.assertTrue(self.game.round <= 5)

    def test_game_history(self):
        self.game.start(rounds=1)
        history = self.game.get_history()
        self.assertTrue(len(history) > 0)

    def test_game_winner(self):
        self.player1.live = 50
        self.player2.live = 0
        winner = self.game.start(rounds=1)
        self.assertEqual(winner, self.player1)

    def test_game_draw(self):
        self.player1.live = 0
        self.player2.live = 0
        winner = self.game.start(rounds=1)
        self.assertIsNone(winner)


if __name__ == '__main__':
    unittest.main()
