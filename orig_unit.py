import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.a1.by/ru/shop/phones/c/smartphones")
        el = driver.find_element(By.CLASS_NAME, "button.button--primary.cookie-panel-button")
        el.click()
        button_element = driver.find_element(By.ID, "product-tile-button_0")
        button_element.click()
        button_element2 = driver.find_element(By.CSS_SELECTOR, ".select2-selection__arrow")
        button_element2.click()
        elem = driver.find_element(By.CSS_SELECTOR, ".select2-search__field")
        elem.send_keys('\ue015')
        elem.send_keys('\ue015')
        elem.send_keys(Keys.ENTER)
        products = driver.find_element(By.CSS_SELECTOR, "h1").text
        products2 = driver.find_element(By.CLASS_NAME, "select2-selection__rendered").text
        self.assertEqual('6 мес по 255,66 руб/мес', products2)
        print("          ")
        print("Выбран", products, "По условиям:", products2)
        self.driver.close()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
