from main.firstGrab_v2_1 import GameBoard
import time
new_game = GameBoard()
new_game.load_game()
while True:
   # input()
    time.sleep(5)
    new_game.analyze_2()
    gems = new_game.find_moves()
    new_game.swap1(gems[0][1], gems[0][2])
    print()

