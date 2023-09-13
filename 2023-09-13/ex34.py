from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestVinodWebsite(unittest.TestCase):

    def test_site_title(self):
        driver = webdriver.Chrome()
        driver.get('https://vinod.co')
        title = driver.title
        self.assertEqual('Learn with Vinod', title)

    def test_should_get_tutorials(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(1)
        driver.get('https://vinod.co')
        elem = driver.find_element(By.LINK_TEXT, 'Tutorials')
        elem.click()
        h5s = driver.find_elements(By.TAG_NAME, 'h5')
        self.assertEqual(len(h5s), 3)


if __name__ == '__main__':
    unittest.main()
