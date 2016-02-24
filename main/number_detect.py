import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np


number_lst = [('number_1.jpg', '1', 0.91) ,('number_2.jpg', '2', 0.8), ('number_3.jpg', '3', 0.8) ,('number_4.jpg', '4', 0.8) , ('number_5.jpg', '5', 0.8), ('number_6.jpg', '6', 0.8), ('number_7.jpg', '7', 0.88), ('number_8.jpg', '8', 0.8), ('number_9.jpg', '9', 0.66),  ('number_0.jpg', '0', 0.88) ]
new_number_lst = []

img_rgb = cv2.imread('Jewels.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

def new_sort(lst, color, param):
    new_lst = []
    #new_lst = sorted(lst, key=lambda x: x[0])
    for i in range(len(lst)):
        is_duplicate = False
        for j in range(len(new_lst)):
            if abs(lst[i][0] - new_lst[j][1][0]) < param and abs(lst[i][1] - new_lst[j][1][1]) < param:
                is_duplicate = True
        if not is_duplicate:
            new_lst.append((color,lst[i]))
    new_lst.sort(key=lambda x: x[1][0])
    return new_lst



for number in number_lst:

    template = cv2.imread(number[0],0)
    w, h = template.shape[::-1]
    print(w, h)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = number[2]
    loc = np.where(res >= threshold)
    lst = []

    for pt in zip(*loc[::-1]):
        lst.append(pt)




    new_number_lst += (new_sort(lst, number[1], 4))



    for i in new_sort(lst, number[1], 4):
        cv2.rectangle(img_rgb, i[1], (i[1][0] + w, i[1][1] + h), (0,0,255), 2)
    cv2.imwrite(number[0][:-4] + '_check.png',img_rgb)


#print(new_number_lst)
for number in new_number_lst:
    if int(number[1][1]) > 280:
        new_number_lst.remove(number)

new_number_lst.sort(key=lambda x: x[1][0])
score = ""
for number in new_number_lst:
    score += number[0]
print(int(score))

print(new_number_lst)