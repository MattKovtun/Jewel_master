import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = cv2.imread('cropped1.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
new_img = img.copy()

cv2.namedWindow('image')


cv2.createTrackbar('H low', 'image', 0, 179, nothing)
cv2.createTrackbar('S low', 'image', 0, 255, nothing)
cv2.createTrackbar('V low', 'image', 0, 255, nothing)

cv2.createTrackbar('H high', 'image', 0, 179, nothing)
cv2.createTrackbar('S high', 'image', 0, 255, nothing)
cv2.createTrackbar('V high', 'image', 0, 255, nothing)


while(1):
    cv2.imshow('image', new_img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    h_low = cv2.getTrackbarPos('H low', 'image')
    s_low = cv2.getTrackbarPos('S low', 'image')
    v_low = cv2.getTrackbarPos('V low', 'image')

    h_high = cv2.getTrackbarPos('H high', 'image')
    s_high = cv2.getTrackbarPos('S high', 'image')
    v_high = cv2.getTrackbarPos('V high', 'image')

    lower = np.array([h_low, s_low, v_low])
    upper = np.array([h_high, s_high, v_high])

    mask = cv2.inRange(hsv, lower, upper)

    new_img = cv2.bitwise_and(img, img, mask=mask)

cv2.destroyAllWindows()