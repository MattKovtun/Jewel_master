from main.firstGrab_v2_1 import GameBoard
import time



#####
# Move this part of code to the separate file
#####
new = GameBoard()

#####
new.load_game() # should be renamed to load_game or something like that
#####

while True:
    try:
        #####
        time.sleep(3) # Do you really need this?
        #####

        new.analyze()
        gems = new.find_moves()
        new.swap1(gems[0][1], gems[0][2])
    except IndexError:
        time.sleep(6)
        continue
