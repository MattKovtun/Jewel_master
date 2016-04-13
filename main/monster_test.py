from main.Jewel_monster_v3 import Game
from Analyzer import SimpleAnalyzer
from MoveDetector import SimpleMove

new_game = Game(SimpleAnalyzer, SimpleMove)
new_game.load()
while True:
   # input()
    #time.sleep(5)
    new_game.analyze()
    gems = new_game.get_move()
    new_game.make_move()
    print()

