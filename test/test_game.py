from platform import node
import pytest

from controller.game import Game
from model.person import Person


@pytest.fixture
def setup_game():
    player1 = Person(with_armor=True)
    player2 = Person()
    game = Game(player1, player2)
    return game, player1, player2


def test_game_initialization(setup_game):
    game, player1, player2 = setup_game
    assert player1.armor is True
    assert player2.armor is False
    assert game.player1 == player1
    assert game.player2 == player2


def test_game_start(setup_game):
    game, player1, player2 = setup_game
    player1.live = 50
    player2.live = 0
    winner = game.start(rounds=1)
    assert winner in [player1, player2]
    assert game.round <= 5


def test_game_history(setup_game):
    game, player1, player2 = setup_game
    game.start(rounds=1)
    history = game.history
    assert len(history) > 0


def test_game_winner(setup_game):
    game, player1, player2 = setup_game
    player1.live = 50
    player2.live = 0
    winner = game.start(rounds=1)
    assert winner == player1


def test_game_draw(setup_game):
    game, player1, player2 = setup_game
    player1.live = 0
    player2.live = 0
    winner = game.start(rounds=1)
    assert winner == None
