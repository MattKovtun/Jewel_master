
from selenium import webdriver
import time
import cv2


driver = webdriver.Firefox()

driver.get('http://www.miniclip.com/games/bejeweled/en/')

el = driver.find_element_by_css_selector('#iframe-game')  # find part of the page you want image of
bd = driver.find_element_by_css_selector('body')

print(el.location)  # location
print(el.size)      # size

print(bd.location)

def connect_start():
    el = driver.find_element_by_css_selector('#iframe-game')
    #time.sleep(30)  # delay to wait while page loaded
    for i in range(30):
        print(30 - i, "seconds left")
        time.sleep(1)
    # Debug message
    print('The page has been loaded.')

    # PLAY jewel button in the middle of the screen is pressed.
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, el.size['width'] // 2, el.size['height'] // 2)
    action.click()
    print(el.size['width'] // 2,el.size['height'] // 2 )
    action.perform()
    time.sleep(3)
    print('click')
    action.move_to_element_with_offset(el, 100, 65)
    action.click()
    action.perform()
    time.sleep(4.5)


connect_start()

def test_switch():
    el = driver.find_element_by_css_selector('#iframe-game')
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, el.size['width'] // 2, el.size['height'] // 2)
    action.click()
    action.move_to_element_with_offset(el, el.size['width'] // 2 + 42, el.size['height'] // 2)
    action.click()

    action.perform()

test_switch()
# ***************************************************************
# You should cut off the image of the game from a screenshot here.
# ***************************************************************

driver.save_screenshot('Jewels.png')  # save screenshot of the image to the file

img = cv2.imread("Jewels.png")
crop_img = img[el.location['y']:el.location['y'] + el.size['height'], el.location['x']:el.location['x'] + el.size['width']]
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
cv2.imwrite("cropped.png", crop_img)
cv2.waitKey(0)







