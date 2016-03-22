from main.firstGrab_v2_1 import GameBoard

new_game = GameBoard()
new_game.load_game()
while True:
    input()
    new_game.analyze_2()