import numpy as np

class Gem:
    def __init__(self, code,  img):
        self.code = code
        self.img = img

    def compare(self, new_img):
        """
        Compare image of this gem with image of gem that is passed.
        :param new_img: image of gem to compare.
        :return: percentage of coincidence.
        """
        res = np.equal(new_img, self.img)
        res = np.prod(res, axis=2).ravel()
        return sum(res) / len(res)

    def __str__(self):
        return self.code
