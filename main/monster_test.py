from Jewel_monster_v3 import Game
from Analyzer import SimpleAnalyzer, KNNAnalyzer
from MoveDetector import SimpleMove, AdvancedMove
import time

new_game = Game(SimpleAnalyzer, AdvancedMove)
new_game.load()
while True:
   # input()
    time.sleep(2)
    new_game.analyze()
    gems = new_game.get_move()
   # input()
    new_game.make_move()
    print()

