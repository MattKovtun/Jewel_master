import os
import numpy as np
import cv2

folders = ['b_', 'r_']

for i in range(folders):
    folder = folders[i]
    num = len(os.listdir(folder)) // 2

    res = np.reshape(np.load(folder + '/0.npy'), -1)

    for i in range(1, num):
        img = np.reshape(np.load(folder + '/' + str(i) + '.npy'), -1)
        cmp = np.equal(img, res)
        res = np.prod([cmp, res], axis=0)
        print(i)

    res = np.reshape(res, (40, 40, 3))
    cv2.imwrite('folders.bmp', res)