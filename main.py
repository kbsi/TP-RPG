
from controller.game import Game
from model.person import Person


player1 = Person("Player 1", with_armor=True)
player2 = Person("Player 2")
game = Game(player1, player2)

winner = game.start(rounds=5)

for history in game.get_history():
    print(history)

if winner:
    print(f'The winner is {winner}')
else:
    print('The game is a draw')
