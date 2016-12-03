import numpy as np
from selenium import webdriver
import time
import cv2
import os




class Game:
    "The bot itself"
    pop_cup = ('start_game.jpg', 0.66)
    ops = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    EXAMPLES_PATH = 'gems_examples/'
    ERRORS = [0.7, 0.7, 0.1]
    EXAMPLES = [['b_.npy', 'g_.npy', 'o_.npy', 'p_.npy', 'r_.npy', 'w_.npy', 'y_.npy'],
                ['bf.npy', 'gf.npy', 'of.npy', 'pf.npy', 'rf.npy', 'wf.npy', 'yf.npy'],
                ['bs.npy', 'gs.npy', 'os.npy', 'ps.npy', 'rs.npy', 'ws.npy', 'ys.npy']]
    MAX = 1000



    def __init__(self, Analyzer, MoveDetector):
        "Strategy pattern used here"

        self.driver = webdriver.Firefox()
        self._analyzer = Analyzer()
        self._move_detector = MoveDetector()

    def analyze(self):
        self.gems = self._analyzer.analyze(self.driver, self)

    def get_move(self):
        self.move = self._move_detector.get_move(self.gems, self)
     #   return self._move_detector.get_move(self.gems)

    def make_move(self):
        """
        Method which in according to detected move, changes placed of gems
        :return:
        """
        el = self.driver.find_element_by_css_selector('#iframe-game')
        gem_1 = self.move[0]
        gem_2 = self.move[1]
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(el, gem_1[0] + 5, gem_1[1] + 5)
        action.click()
        time.sleep(0.4)
        action.move_to_element_with_offset(el, gem_2[0] + 5, gem_2[1] + 5)
        action.click()
        action.perform()

    def load(self):
        return self._load()



    def _load(self):
        """
        Method which loads specific web page with the gama
        :return:
        """
        #driver = webdriver.Firefox()
        self.driver.get('http://www.miniclip.com/games/bejeweled/en/')

        ####
        el = self.driver.find_element_by_css_selector('#iframe-game')  # you should use meaningful names
        ####

        print('The page has been loaded.')
        while True:
            self.driver.save_screenshot('Jewels.png')  # save screenshot of the image to the file
            img = cv2.imread("Jewels.png")
            crop_img = img[el.location['y']: el.location['y'] + el.size['height'],
                       el.location['x']: el.location['x'] + el.size['width']]
            cv2.imwrite("cropped.png", crop_img)
            # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
            img_rgb = cv2.imread("cropped.png")
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            # cv2.waitKey(0)

            template = cv2.imread(Game.pop_cup[0], 0)
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = Game.pop_cup[1]
            loc = np.where(res >= threshold)
            lst = []

            for pt in zip(*loc[::-1]):
                lst.append(pt)
            print("The game is loading, please wait...")  # debug

            if len(lst):
                print("Loading is completed!")
                break
            else:
                continue


        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(el, el.size['width'] // 2, el.size['height'] // 2)
        action.click()
        #  print(el.size['width'] // 2,el.size['height'] // 2 )
        action.perform()
        time.sleep(3)
        print('click')
        action.move_to_element_with_offset(el, 100, 65)
        action.click()
        action.perform()
        time.sleep(4.5)



    @staticmethod
    def save_example(folder, img):
        """
        Check folder existence. If folder doesn't exist it creates new folder.
        And saves gems to that folder
        :param folder: path to folder.
        :param img: image file.
        :return: number of files in folder.
        """
        np_filename = folder
        im_filename = folder
        if os.path.isdir(folder):
            num = str(len(os.listdir(folder)) // 2)
            im_filename += '/' + num + '.jpg'
            np_filename += '/' + num + '.npy'
        else:
            os.mkdir(folder)
            im_filename += '/0.jpg'
            np_filename += '/0.npy'

        num = len(os.listdir(folder)) // 2

        if num <= Game.MAX:
            for i in range(num):
                saved = np.load(folder + '/' + str(i) + '.npy')

                if (saved == img).all():
                    return

            cv2.imwrite(im_filename, img)
            np.save(np_filename, img)
