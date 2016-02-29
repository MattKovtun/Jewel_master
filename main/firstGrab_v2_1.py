
import numpy as np

import copy
from selenium import webdriver
import time
import cv2



class GameBoard:
  #  number_lst = [('number_1.jpg', '1', 0.88) ,('number_2.jpg', '2', 0.8), ('number_3.jpg', '3', 0.8) ,('number_4.jpg', '4', 0.8) , ('number_5.jpg', '5', 0.8), ('number_6.jpg', '6', 0.8), ('number_7.jpg', '7', 0.88), ('number_8.jpg', '8', 0.8), ('number_9.jpg', '9', 0.66),  ('number_0.jpg', '0', 0.8) ]
  #  new_number_lst = []

    gems = [('White_gem.jpg', 'white', 0.8), ('Blue_gem.jpg', 'blue', 0.8), ('Purple_gem.jpg', 'purple', 0.8), ('Yellow_gem.jpg', 'yellow', 0.8), ('Red_gem.jpg', 'red', 0.8), ('Orange_gem.jpg', 'orange', 0.83), ('Green_gem.jpg', 'green', 0.82), ('Green_flame.jpg', 'green_flame', 0.8), ('Blue_flame.jpg', 'blue_flame', 0.8), ('Yellow_flame.jpg', 'yellow_flame', 0.8)]
    ops = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def __init__(self, driver=webdriver.Firefox()):

        self.driver = driver
  # find part of the page you want image of

    def detect(self, mat):
        """
        We detect here 3 in row or 3 in column
        """
        for j in range(8):
            for i in range(1, 8):

                #if mat[j][i][0] != mat[j][i - 1][0] : #if lst[i][j] != lst[i][j + 1]:
                #    continue

                if i == 7:
                    continue


                if mat[j][i][0] == mat[j][i - 1][0] and mat[j][i][0] == mat[j][i + 1][0]:
                   # print("Line at ", j, i - 1, mat[j][i - 1], mat[j][i + 1])
                    return True
        for j in range(8):
            for i in range(1, 8):

                if i == 7:
                    continue

                if mat[i][j][0] == mat[i - 1][j][0] and mat[i][j][0] == mat[i + 1][j][0]:
                  #  print("Line at ", i - 1, j, mat[i - 1][j], mat[i + 1][j])
                    return True

    def connect_start(self):
        self.driver.get('http://www.miniclip.com/games/bejeweled/en/')
        self.el = self.driver.find_element_by_css_selector('#iframe-game')

        for i in range(30):
            print(30 - i, "seconds left")
            time.sleep(1)
    # Debug message
        print('The page has been loaded.')
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

    def analyze(self):

        self.mat_lst = []
        self.general_lst = []
        self.driver.save_screenshot('Jewels.png')  # save screenshot of the image to the file
        self.img = cv2.imread("Jewels.png")
        self.crop_img = self.img[self.el.location['y']:self.el.location['y'] + self.el.size['height'], self.el.location['x']:self.el.location['x'] + self.el.size['width']]
        cv2.imwrite("cropped.png", self.crop_img)
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
        self.img_rgb = cv2.imread("cropped.png")
        self.img_gray = cv2.cvtColor(self.img_rgb, cv2.COLOR_BGR2GRAY)
        cv2.waitKey(0)



        for self.gem in GameBoard.gems:
            self.template = cv2.imread(self.gem[0],0)
            #w, h = template.shape[::-1]
           # print(w, h)
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
       # print(self.mat_lst)
        return self.mat_lst


    def new_sort(self, lst, color, param):
        #self.lst = lst
       #self.color = color
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
          #  print(i, j, mat_lst[i][j])

            self.new_mat_lst = copy.deepcopy(self.mat_lst)

            for self.op in GameBoard.ops:
                self.n_i = self.i + self.op[0]
                self.n_j = self.j + self.op[1]
                #print(n_i ,n_j)
                if 0 <= self.n_i <= 7 and 0 <= self.n_j <= 7:
                    self.swap = self.new_mat_lst[self.i][self.j]
                    self.new_mat_lst[self.i][self.j] = self.new_mat_lst[self.n_i][self.n_j]
                    self.new_mat_lst[self.n_i][self.n_j] = self.swap

                    if GameBoard.detect(self, self.new_mat_lst):
                        if ((self.n_i, self.n_j), (self.i, self.j)) not in self.moves:
                           # self.moves.append(((self.i, self.j), (self.n_i, self.n_j)))
                            self.moves.append(((self.mat_lst[self.i][self.j]), (self.mat_lst[self.n_i][self.n_j])))

                    self.swap = self.new_mat_lst[self.n_i][self.n_j]
                    self.new_mat_lst[self.n_i][self.n_j] = self.new_mat_lst[self.i][self.j]
                    self.new_mat_lst[self.i][self.j] = self.swap
        return self.moves

    def swap1(self, gem_1, gem_2):
        self.gem_1 = gem_1
        self.gem_2 = gem_2
        self.action.move_to_element_with_offset(self.el, self.gem_1[1][0], self.gem_1[1][1])
        self.action.click()
        self.action.move_to_element_with_offset(self.el, self.gem_2[1][0], self.gem_2[1][1])
        self.action.click()
        self.action.perform()


new = GameBoard()
new.connect_start()
new.analyze()
new.find_moves()


#print(list(gems[0]))
gems = new.find_moves()

new.swap1(gems[0][0], gems[0][1])
