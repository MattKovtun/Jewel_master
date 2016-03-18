import cv2
import numpy as np


img = cv2.imread('Green_gem.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
new_img = img.copy()

cv2.namedWindow('image')





h_low = 0
s_low = 0
v_low = 118

h_high = 179
s_high = 255
v_high = 255

lower = np.array([h_low, s_low, v_low])
upper = np.array([h_high, s_high, v_high])

mask = cv2.inRange(hsv, lower, upper)

new_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('image', new_img)
cv2.imwrite("cropped1.png"   , new_img)

cv2.waitKey(0)


