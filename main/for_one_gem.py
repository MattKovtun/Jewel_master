import cv2
import numpy as np
#from matplotlib import pyplot as plt
import numpy as np
#import detect

gems = [('number_1.jpg', '1', 0.91) ,('number_2.jpg', '2', 0.8), ('number_3.jpg', '3', 0.8) ,('number_4.jpg', '4', 0.8) , ('number_5.jpg', '5', 0.8), ('number_6.jpg', '6', 0.8), ('number_7.jpg', '7', 0.88), ('number_8.jpg', '8', 0.88), ('number_9.jpg', '9', 0.76),  ('number_0.jpg', '0', 0.8) ]
general_lst = []
pop_cup = [('start_game.jpg','test', 0.66)]

img_rgb = cv2.imread('test_play.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

def sorter(lst, color):
    new_lst = []
    lst = sorted(lst, key=lambda x: x[0])
    #print(lst)
    for i in range(len(lst) - 1):
        if abs(lst[i][0] - lst[i + 1][0]) > 10 or abs(lst[i][1] - lst[i + 1][1]) > 10:
            new_lst.append(lst[i])
    new_lst.append(lst[-1])
   # print(new_lst)
            
    new_lst = sorted(new_lst, key=lambda x: x[1])
    lst = []
    for i in range(len(new_lst) - 1):
        if abs(new_lst[i][0] - new_lst[i + 1][0]) > 10 or abs(new_lst[i][1] - new_lst[i + 1][1]) > 10:
            lst.append((color ,new_lst[i]))
    lst.append((color ,new_lst[-1]))
    #print(lst)
    return lst
        
def new_sort(lst, color):
    new_lst = []
    #new_lst = sorted(lst, key=lambda x: x[0])
    for i in range(len(lst)):
        is_duplicate = False
        for j in range(len(new_lst)):
            if abs(lst[i][0] - new_lst[j][1][0]) < 4 and abs(lst[i][1] - new_lst[j][1][1]) < 4:
                is_duplicate = True
        if not is_duplicate:
            new_lst.append((color,lst[i]))
    new_lst.sort(key=lambda x: x[1][0])    
    return new_lst
          
            
    
for gem in pop_cup:

    template = cv2.imread(gem[0],0)
    w, h = template.shape[::-1]
    print(w, h)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = gem[2]
    loc = np.where(res >= threshold)
    lst = []

    for pt in zip(*loc[::-1]):
        lst.append(pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
       
    
    general_lst += (new_sort(lst, gem[1]))

    for i in new_sort(lst, gem[1]):
        cv2.rectangle(img_rgb, i[1], (i[1][0] + w, i[1][1] + h), (0,0,255), 2)
    cv2.imwrite(gem[0][:-4] + '_check.png',img_rgb)

general_lst.sort(key=lambda x: x[1][0])
mat_lst = []
print(len(general_lst))
print(general_lst)
for i in range(0,len(general_lst) - 7, 8):
    part = general_lst[i:i + 8]
    part.sort(key=lambda x: x[1][0])
    mat_lst.append(part)
#print(general_lst[:8])
print(mat_lst)
