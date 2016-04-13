import cv2
from main.gem import Gem
import numpy as np
#from Jewel_monster_v3 import Game

#
# class AbstractAnalyzer:
#     def __init__(self):
#         self.EXAMPLES = [['b_.npy', 'g_.npy', 'o_.npy', 'p_.npy', 'r_.npy', 'w_.npy', 'y_.npy'],
#                                     ['bf.npy', 'gf.npy', 'of.npy', 'pf.npy', 'rf.npy', 'wf.npy', 'yf.npy'],
#                                     ['bs.npy', 'gs.npy', 'os.npy', 'ps.npy', 'rs.npy', 'ws.npy', 'ys.npy']]
#         self.EXAMPLES_PATH = 'gems_examples/'
#         self.ERRORS = [0.7, 0.7, 0.1]

class KNNAnalyzer:
    pass

class SimpleAnalyzer:

    def _clear_data(self):
        self.gems = []
        for i in range(8):
            level = []
            for j in range(8):
                level.append('__')
            self.gems.append(level)

    def analyze(self, driver, Game):
      #  coords = []

        self.gems = []
        examples = []


        el = driver.find_element_by_css_selector('#iframe-game')  # you should use meaningful names

        driver.save_screenshot('temp.bmp')
        screen = cv2.imread("temp.bmp")
        top = el.location['y'] + 49
        left = el.location['x'] + 168
        width = 320
        height = 320

        board = screen[top:top + height, left:left + width]
        hsv = cv2.cvtColor(board, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 0, 118])
        upper = np.array([179, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        filtered_board = cv2.bitwise_and(board, board, mask=mask)

        self._clear_data()

        for i in range(8):
            level = []
            for j in range(8):
                level.append('__')
            self.gems.append(level)
         #   coords.append(level)
        # Adding file examples
        for level in Game.EXAMPLES:
            examples_level = []
            for filename in level:
                img = np.load(Game.EXAMPLES_PATH + filename)
                code = filename[:-4]
                examples_level.append(Gem(code, img))
            examples.append(examples_level)



        for i in range(8):
            for j in range(8):
                found = False
                gem = filtered_board[i * 40:(i + 1) * 40, j * 40:(j + 1) * 40]
                full_gem = board[i * 40:(i + 1) * 40, j * 40:(j + 1) * 40]
              #  coords[i][j] = ((j * 40) + 5 + 168, (i * 40) + 5 + 49)
                for k in range(len(examples)):
                    if found:
                        break
                        #  print(self.examples)
                        #  print()
                    level = examples[k]
                    # print(level)

                    for example in level:
                        res = example.compare(gem)
                        if res > Game.ERRORS[k]:
                            self.gems[i][j] = str(example)
                            Game.save_example(str(example), full_gem)  ###########################

                            #                            self.mat_lst.append()
                            found = True
                            break

                if self.gems[i][j] == '__':
                    Game.save_example('errors', full_gem)

            print(' '.join(self.gems[i]))
            # print(self.coords)
            # print(self.gems)
        return self.gems
        # cv2.imshow('board', self.board_img)
        # cv2.waitKey(0)