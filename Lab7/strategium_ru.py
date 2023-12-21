import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()  # Используйте путь к драйверу, если он не установлен в PATH
        self.driver.get("https://www.strategium.ru/")

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(5)
        # Проверка, что результаты поиска появились на странице
        results = self.driver.find_elements_by_css_selector('.result')
        self.assertGreater(len(results), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()