import numpy as np
import cv2
from saver import save_file

img = cv2.imread('img00001.bmp')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
input_dat = open("10676.dat", encoding='WINDOWS-1251')
data = []

space = 1
for line in input_dat:
    if len(line) == 1:
        print("he")
        space = 0
    space += 1
    if space == 3:
        line = line.strip()
        data.append(line)

print(data)

img_h, img_w = img_gray.shape
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
new_img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(img_w, img_h)


(c_x_0, c_y_0), r_0 = cv2.minEnclosingCircle(contours[0])

top_left = (0, c_x_0, c_y_0)
top_right = (0, c_x_0, c_y_0)
bottom_left = (0, c_x_0, c_y_0)
bottom_right = (0, c_x_0, c_y_0)


#print(len(contours))
lst = []

for i in range(len(contours)):
    contour = contours[i]
    (c_x, c_y), r = cv2.minEnclosingCircle(contour)

    if c_x + c_y < top_left[1] + top_left[2]:
        top_left = (i, c_x, c_y)
    if c_y - c_x <  top_right[2] - top_right[1]:
        top_right = (i, c_x, c_y)
    if c_x - c_y <  bottom_left[1] - bottom_left[2]:
        bottom_left = (i, c_x, c_y)
    if  c_x + c_y >  bottom_right[1] +  bottom_right[2]:
        bottom_right = (i, c_x, c_y)


    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #lst.append(abs(x) + abs(y))

pts1 = np.float32([[bottom_left[1], bottom_left[2]],[bottom_right[1], bottom_right[2]],[top_left[1], top_left[2]]])
pts2 = np.float32([[0,0], [0, 1200], [800, 0]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img, M, (800, 85))

for i in range(len(letter)):
   # cv2.rectangle(dst, (262 + i * 27, 47), (289 + i * 27, 83), (0, 0, 255), 1)

    save_file("test", dst[47 : 83, 262 + i * 27: 289 + i * 27 ], letter[i])
    dst = cv2.warpAffine(img, M, (800, 85))

cv2.imshow("header", dst)
cv2.waitKey(0)
