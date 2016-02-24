import unittest
#from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains  import ActionChains

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        #click = driver.drag_and_drop_by_offset(100,100)

        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(100,100,120)
        actions.perform()


        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

        print(Keys.RETURN)
    #def tearDown(self):
       # self.driver.close()

if __name__ == "__main__":
    unittest.main()