import unittest
from selenium import webdriver
from pages_.logInPage import LoginPage
from pages_.navigationBar import NavigationBar
from time import sleep


class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://us.puma.com/us/en")

    def test_search_product(self):
        navigationBarObject = NavigationBar(self.driver)
        navigationBarObject.click_to_search_field_button()
        navigationBarObject.fill_search_field_element("CA Pro Lux Soft Sneakers")
        navigationBarObject.click_to_search_button()


    def tearDown(self):
        self.driver.close()