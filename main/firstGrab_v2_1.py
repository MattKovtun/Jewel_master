import numpy as np
import time
import copy
from selenium import webdriver
import time
import cv2
import os
from main.gem import Gem


class GameBoard:
      #  number_lst = [('number_1.jpg', '1', 0.88) ,('number_2.jpg', '2', 0.8), ('number_3.jpg', '3', 0.8) ,('number_4.jpg', '4', 0.8) , ('number_5.jpg', '5', 0.8), ('number_6.jpg', '6', 0.8), ('number_7.jpg', '7', 0.88), ('number_8.jpg', '8', 0.8), ('number_9.jpg', '9', 0.66),  ('number_0.jpg', '0', 0.8) ]
  #  new_number_lst = []
    pop_cup = ('start_game.jpg', 0.66)
    gems = [('White_gem_1.jpg', 'white', 0.88), ('White_flame_1.jpg', 'white_flame', 0.88), ('White_snow_1.jpg', 'white_snow', 0.88), ('Blue_gem_1.jpg', 'blue', 0.84), ('Blue_snow_1.jpg', 'blue_snow', 0.82), ('Purple_gem_1.jpg', 'purple', 0.8), ('Purple_flame_1.jpg', 'purple_flame', 0.8), ('Purple_snow_1.jpg', 'purple_snow', 0.8), ('Yellow_gem_1.jpg', 'yellow', 0.82),  ('Yellow_snow_1.jpg', 'yellow_snow', 0.88), ('Red_gem_1.jpg', 'red', 0.81), ('Red_flame_1.jpg', 'red_flame', 0.8),  ('Red_snow_1.jpg', 'red_snow', 0.8), ('Orange_gem_1.jpg', 'orange', 0.85), ('Orange_flame_1.jpg', 'orange_flame', 0.85), ('Orange_snow_1.jpg', 'orange_snow', 0.83), ('Green_gem_1.jpg', 'green', 0.84), ('Green_flame_1.jpg', 'green_flame', 0.8), ('Green_snow_1.jpg', 'green_snow', 0.8), ('Blue_flame_1.jpg', 'blue_flame', 0.8), ('Yellow_flame_1.jpg', 'yellow_flame', 0.84)]
    #gems = [('White_gem.jpg', 'white', 0.88), ('White_flame.jpg', 'white_flame', 0.88), ('White_snow.jpg', 'white_snow', 0.88), ('Blue_gem.jpg', 'blue', 0.84), ('Blue_snow.jpg', 'blue_snow', 0.82), ('Purple_gem.jpg', 'purple', 0.8), ('Purple_flame.jpg', 'purple_flame', 0.8), ('Purple_snow.jpg', 'purple_snow', 0.8), ('Yellow_gem.jpg', 'yellow', 0.82),  ('Yellow_snow.jpg', 'yellow_snow', 0.88), ('Red_gem.jpg', 'red', 0.81), ('Red_flame.jpg', 'red_flame', 0.8),  ('Red_snow.jpg', 'red_snow', 0.8), ('Orange_gem.jpg', 'orange', 0.85), ('Orange_flame.jpg', 'orange_flame', 0.85), ('Orange_snow.jpg', 'orange_snow', 0.83), ('Green_gem.jpg', 'green', 0.84), ('Green_flame.jpg', 'green_flame', 0.8), ('Green_snow.jpg', 'green_snow', 0.8), ('Blue_flame.jpg', 'blue_flame', 0.8), ('Yellow_flame.jpg', 'yellow_flame', 0.84)]

    ops = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    EXAMPLES_PATH = 'gems_examples/'
    ERRORS = [0.7, 0.7]
    EXAMPLES = [['b_.npy', 'g_.npy', 'o_.npy', 'p_.npy', 'r_.npy', 'w_.npy', 'y_.npy'],
                ['bf.npy', 'gf.npy', 'of.npy', 'pf.npy', 'rf.npy', 'wf.npy', 'yf.npy']]

    def __init__(self, driver=webdriver.Firefox()):
        self.driver = driver
        self.examples = []

        self.gems = []
        for i in range(8):
            level = []
            for j in range(8):
                level.append('__')
            self.gems.append(level)
        # Adding file examples
        for level in GameBoard.EXAMPLES:
            examples_level = []
            for filename in level:
                img = np.load(GameBoard.EXAMPLES_PATH + filename)
                code = filename[:-4]
                examples_level.append(Gem(code, img))
            self.examples.append(examples_level)

    def _clear_data(self):
        self.gems = []
        for i in range(8):
            level = []
            for j in range(8):
                level.append('__')
            self.gems.append(level)

    def detect(mat):
        """
        We detect here 3 in row or 3 in column
        """
       # print(len(mat))
        utility = 0

        for j in range(8):
            for i in range(1, 8):
                #if mat[j][i][0] != mat[j][i - 1][0] : #if lst[i][j] != lst[i][j + 1]:
                    #continue
                if i == 7 and utility >= 2:
                    return (True, utility)

                if i == 7:
                    utility = 0
                    continue

                if mat[j][i][0][:3] == mat[j][i - 1][0][:3]:
                     utility +=1

                if mat[j][i][0][:3] != mat[j][i - 1][0][:3]:
                    if utility >= 2:
                        return (True, utility)
                    else:
                        utility = 0



                  #  print("Line at ", j, i - 1, mat[j][i - 1], mat[j][i + 1])
                   # return True


               # if mat[j][i][0][:3] == mat[j][i - 1][0][:3] and mat[j][i][0][:3] == mat[j][i + 1][0][:3]:

                  #  print("Line at ", j, i - 1, mat[j][i - 1], mat[j][i + 1])
                   # return True

        utility = 0
        for j in range(8):
            for i in range(1, 8):
                if i == 7 and utility >= 2:
                    return (True, utility)

                if i == 7:
                    utility = 0
                    continue

                if mat[i][j][0][:3] == mat[i - 1][j][0][:3]:
                    utility +=1
                  #  print("Line at ", i - 1, j, mat[i - 1][j], mat[i + 1][j])
                if mat[i][j][0][:3] != mat[i - 1][j][0][:3]:
                    if utility >= 2:
                        return (True, utility)
                    else:
                        utility = 0

        return (False, 0)

    def connect_start(self):
        self.driver.get('http://www.miniclip.com/games/bejeweled/en/')

        ####
        self.el = self.driver.find_element_by_css_selector('#iframe-game') # you should use meaningful names
        ####

        print('The page has been loaded.')
        while True:
            if self.start_game():
                print("SS")
                break

        self.action = webdriver.common.action_chains.ActionChains(self.driver)
        self.action.move_to_element_with_offset(self.el, self.el.size['width'] // 2, self.el.size['height'] // 2)
        self.action.click()
      #  print(el.size['width'] // 2,el.size['height'] // 2 )
        self.action.perform()
        time.sleep(3)
        print('click')
        self.action.move_to_element_with_offset(self.el, 100, 65)
        self.action.click()
        self.action.perform()
        time.sleep(4.5)

    @staticmethod
    def save_file(folder, img):
        """
        Check folder existence. If folder doesn't exist it creates new folder.
        :param folder: path to folder.
        :param img: image file.
        :return: number of files in folder.
        """
        np_filename = folder
        im_filename = folder
        if os.path.isdir(folder):
            num = str(len(os.listdir(folder)))
            os.mkdir(folder + '/' + num)
            im_filename += '/' + num + '/data.jpg'
            np_filename += '/' + num + '/data.npy'
        else:
            os.mkdir(folder)
            os.mkdir(folder + '/0')
            im_filename += '/0/data.jpg'
            np_filename += '/0/data.npy'
        cv2.imwrite(im_filename, img)
        np.save(np_filename, img)

    def analyze_2(self):
        self.driver.save_screenshot('temp.jpg')
        screen = cv2.imread("temp.jpg")
        top = self.el.location['y'] + 49
        left = self.el.location['x'] + 168
        width = 320
        height = 320

        img_board = screen[top:top + height, left:left + width]

        hsv = cv2.cvtColor(img_board, cv2.COLOR_BGR2HSV)

        lower = np.array([0, 0, 118])
        upper = np.array([179, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        img_board = cv2.bitwise_and(img_board, img_board, mask=mask)

        self._clear_data()

        for i in range(8):
            for j in range(8):
                found = False
                gem = img_board[i * 40:(i + 1) * 40, j * 40:(j + 1) * 40]

                for k in range(len(self.examples)):
                    if found:
                        break

                    level = self.examples[k]
                    for example in level:
                        res = example.compare(gem)
                        if res > GameBoard.ERRORS[k]:
                            self.gems[i][j] = str(example)
                            found = True
                            break

                if self.gems[i][j] == '__':
                    GameBoard.save_file('errors', gem)

            print(' '.join(self.gems[i]))

        #cv2.imshow('board', self.board_img)
        #cv2.waitKey(0)

    def analyze(self):
        self.mat_lst = []
        self.general_lst = []

        self.driver.save_screenshot('Jewels.png')  # save screenshot of the image to the file

        #####
        self.img = cv2.imread("Jewels.png") # why do you need to save this picture?
        #####

        self.crop_img = self.img[self.el.location['y']:self.el.location['y'] + self.el.size['height'], self.el.location['x']:self.el.location['x'] + self.el.size['width']]

      #  img = cv2.imread(gem)
        hsv = cv2.cvtColor(self.crop_img, cv2.COLOR_BGR2HSV)

        lower = np.array([0, 0, 118])
        upper = np.array([179, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        self.crop_image = cv2.bitwise_and(self.crop_img, self.crop_img, mask=mask)










        cv2.imwrite("cropped.png"   , self.crop_image)
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
        self.img_rgb = cv2.imread("cropped.png")
        self.img_gray = cv2.cvtColor(self.img_rgb, cv2.COLOR_BGR2GRAY)
        #cv2.waitKey(0)

        for self.gem in GameBoard.gems:
            self.template = cv2.imread(self.gem[0],0)
            self.res = cv2.matchTemplate(self.img_gray, self.template, cv2.TM_CCOEFF_NORMED)
            self.threshold = self.gem[2]
            self.loc = np.where(self.res >= self.threshold)
            self.lst = []

            for self.pt in zip(*self.loc[::-1]):
                self.lst.append(self.pt)

            self.general_lst += (GameBoard.new_sort(self, self.lst, self.gem[1], 10))
        #   self.bd = self.driver.find_element_by_css_selector('body')
        #print(len(self.general_lst))
        self.general_lst.sort(key=lambda x: x[1][1])

        for i in range(0,len(self.general_lst) - 7, 8):
            self.part = self.general_lst[i:i + 8]
            self.part.sort(key=lambda x: x[1][0])
            self.mat_lst.append(self.part)
      #  print(len(self.mat_lst))
        return self.mat_lst


    def new_sort(self, lst, color, param):
        self.param = param
        self.new_lst = []

        for i in range(len(lst)):
            self.is_duplicate = False
            for j in range(len(self.new_lst)):
                if abs(lst[i][0] - self.new_lst[j][1][0]) < self.param and abs(lst[i][1] - self.new_lst[j][1][1]) < self.param:
                    self.is_duplicate = True
            if not self.is_duplicate:
                self.new_lst.append((color, self.lst[i]))
        self.new_lst.sort(key=lambda x: x[1][0])
        return self.new_lst

    def find_moves(self):
        self.moves = []
        for self.cell in range(64):
            self.i = self.cell // 8
            self.j = self.cell - self.i * 8
            print()
            print(self.i, self.j, self.mat_lst[self.i][self.j])
            self.new_mat_lst = copy.deepcopy(self.mat_lst)

            for self.op in GameBoard.ops:
                self.n_i = self.i + self.op[0]
                self.n_j = self.j + self.op[1]
                #print(n_i ,n_j)
                if 0 <= self.n_i <= 7 and 0 <= self.n_j <= 7:
                    self.swap = self.new_mat_lst[self.i][self.j]
                    self.new_mat_lst[self.i][self.j] = self.new_mat_lst[self.n_i][self.n_j]
                    self.new_mat_lst[self.n_i][self.n_j] = self.swap
                    self.TM = GameBoard.detect(self.new_mat_lst)
                    if self.TM[0]:
                        if (self.TM[0], (self.n_i, self.n_j), (self .i, self.j)) not in self.moves:
                           # self.moves.append(((self.i, self.j), (self.n_i, self.n_j)))
                            self.moves.append((self.TM[1], (self.mat_lst[self.i][self.j]), (self.mat_lst[self.n_i][self.n_j])))

                    self.swap = self.new_mat_lst[self.n_i][self.n_j]
                    self.new_mat_lst[self.n_i][self.n_j] = self.new_mat_lst[self.i][self.j]
                    self.new_mat_lst[self.i][self.j] = self.swap

       # print(len(self.moves))
        print(self.moves)
        self.moves = sorted(self.moves, reverse=True, key=lambda x: x[0])

        return self.moves

    def swap1(self, gem_1, gem_2):
        self.action = webdriver.common.action_chains.ActionChains(self.driver)
        self.gem_1 = gem_1
        self.gem_2 = gem_2
        self.action.move_to_element_with_offset(self.el, self.gem_1[1][0] + 4, self.gem_1[1][1] + 4)
        self.action.click()
        time.sleep(0.4)
        self.action.move_to_element_with_offset(self.el, self.gem_2[1][0] + 4, self.gem_2[1][1] + 4)
        self.action.click()
        self.action.perform()

    def start_game(self):
        self.driver.save_screenshot('Jewels.png')  # save screenshot of the image to the file
        self.img = cv2.imread("Jewels.png")
        self.crop_img = self.img[self.el.location['y']:self.el.location['y'] + self.el.size['height'], self.el.location['x']:self.el.location['x'] + self.el.size['width']]
        cv2.imwrite("cropped.png"   , self.crop_img)
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
        self.img_rgb = cv2.imread("cropped.png")
        self.img_gray = cv2.cvtColor(self.img_rgb, cv2.COLOR_BGR2GRAY)
       # cv2.waitKey(0)

        self.template = cv2.imread(GameBoard.pop_cup[0], 0)
        self.res = cv2.matchTemplate(self.img_gray, self.template,cv2.TM_CCOEFF_NORMED)
        self.threshold = GameBoard.pop_cup[1]
        self.loc = np.where(self.res >= self.threshold)
        self.lst = []

        for self.pt in zip(*self.loc[::-1]):
            self.lst.append(self.pt)
        print("It's loading ,wait please...") #debug

        if len(self.lst) :
            print("Loading is completed!")
            return True
        else :
            return False

"""
#####
# Move this part of code to the separate file
#####
new = GameBoard()

#####
new.connect_start() # should be renamed to load_game or something like that
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
"""