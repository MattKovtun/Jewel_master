import os
import cv2
import numpy as np
def save_file(folder, img, letter):
    """
    Check folder existence. If folder doesn't exist it creates new folder.
    :param folder: path to folder.
    :param img: image file.
    :return: number of files in folder.
    """
    np_filename = folder
    im_filename = folder
    if os.path.isdir(folder):
        letter = str(letter)
        if os.path.isdir(folder + '/' + letter):
            num = str(len(os.listdir(folder + '/' + letter)) // 2)
            im_filename += '/' + letter + '/' + num + '.jpg'
            np_filename += '/' + letter + '/' + num + '.npy'
        else:

            os.mkdir(folder + '/' + letter)
            im_filename += '/' + letter + '/' + '0' + '.jpg'
            np_filename += '/' + letter + '/' + '0' + '.npy'
    cv2.imwrite(im_filename, img)
    np.save(np_filename, img)
