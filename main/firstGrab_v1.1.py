import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy


number_lst = [('number_1.jpg', '1', 0.88) ,('number_2.jpg', '2', 0.8), ('number_3.jpg', '3', 0.8) ,('number_4.jpg', '4', 0.8) , ('number_5.jpg', '5', 0.8), ('number_6.jpg', '6', 0.8), ('number_7.jpg', '7', 0.88), ('number_8.jpg', '8', 0.8), ('number_9.jpg', '9', 0.66),  ('number_0.jpg', '0', 0.8) ]
new_number_lst = []

gems = [('White_gem.jpg', 'white', 0.8), ('Blue_gem.jpg', 'blue', 0.8), ('Purple_gem.jpg', 'purple', 0.8), ('Yellow_gem.jpg', 'yellow', 0.8), ('Red_gem.jpg', 'red', 0.8), ('Orange_gem.jpg', 'orange', 0.8), ('Green_gem.jpg', 'green', 0.82), ('Green_flame.jpg', 'green_flame', 0.8), ('Blue_flame.jpg', 'blue_flame', 0.8), ('Yellow_flame.jpg', 'yellow_flame', 0.8)]
general_lst = []

img_rgb = cv2.imread('Jewels_2.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


def new_sort(lst, color, param):
    new_lst = []
    for i in range(len(lst)):
        is_duplicate = False
        for j in range(len(new_lst)):
            if abs(lst[i][0] - new_lst[j][1][0]) < param and abs(lst[i][1] - new_lst[j][1][1]) < param:
                is_duplicate = True
        if not is_duplicate:
            new_lst.append((color,lst[i]))
    new_lst.sort(key=lambda x: x[1][0])    
    return new_lst
          
            
    
for gem in gems:
    template = cv2.imread(gem[0],0)
    w, h = template.shape[::-1]
    print(w, h)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = gem[2]
    loc = np.where(res >= threshold)
    lst = []
    
    for pt in zip(*loc[::-1]):
        lst.append(pt)
    
    general_lst += (new_sort(lst, gem[1], 10))
        
   # for i in new_sort(lst, gem[1]):
    #    cv2.rectangle(img_rgb, i[1], (i[1][0] + w, i[1][1] + h), (0,0,255), 2)
    #cv2.imwrite(gem[0][:-4] + '.png',img_rgb)

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


for number in new_number_lst:
    if int(number[1][1]) > 280:
        new_number_lst.remove(number)


new_number_lst.sort(key=lambda x: x[1][0])
score = ""

general_lst.sort(key=lambda x: x[1][1])
mat_lst = []


for number in new_number_lst:
    score += number[0]


for i in range(0,len(general_lst) - 7, 8):
    part = general_lst[i:i + 8]
    part.sort(key=lambda x: x[1][0])
    mat_lst.append(part)


print(new_number_lst)





ops = [(-1, 0), (1, 0), (0, -1), (0, 1)]
moves = []

def detect(mat):
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
                print("Line at ", j, i - 1, mat[j][i - 1], mat[j][i + 1])
                return True
    for j in range(8):
        for i in range(1, 8):

            if i == 7:
                continue

            if mat[i][j][0] == mat[i - 1][j][0] and mat[i][j][0] == mat[i + 1][j][0]:
                print("Line at ", i - 1, j, mat[i - 1][j], mat[i + 1][j])
                return True


print(mat_lst)
for cell in range(64):
    i = cell // 8
    j = cell - i * 8
    print(i, j, mat_lst[i][j])
    
    new_mat_lst = copy.deepcopy(mat_lst)
    
    for op in ops:
        n_i = i + op[0]
        n_j = j + op[1]
        #print(n_i ,n_j)
        if 0 <= n_i <= 7 and 0 <= n_j <= 7:
            swap = new_mat_lst[i][j]
            new_mat_lst[i][j] = new_mat_lst[n_i][n_j]
            new_mat_lst[n_i][n_j] = swap

            if detect(new_mat_lst):
                if ((n_i, n_j), (i, j)) not in moves:
                    moves.append(((i, j), (n_i, n_j)))

            swap = new_mat_lst[n_i][n_j]
            new_mat_lst[n_i][n_j] = new_mat_lst[i][j]
            new_mat_lst[i][j] = swap
print(moves)


print(int(score))