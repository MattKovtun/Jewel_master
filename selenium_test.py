from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get('http://www.miniclip.com/games/bejeweled/en/')

el = driver.find_element_by_css_selector('#iframe-game')  # find part of the page you want image of

print(el.location)  # location
print(el.size)      # size

driver.save_screenshot('Jewels.png')  # save screenshot of the image to the file

# ***************************************************************
# You should cut off the image of the game from a screenshot here.
# ***************************************************************

time.sleep(60)  # delay to wait while page loaded

# Debug message
print('The page has been loaded.')

# PLAY jewel button in the middle of the screen is pressed.
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(el, el.size['width'] // 2, el.size['height'] // 2)
action.click()
action.perform()
