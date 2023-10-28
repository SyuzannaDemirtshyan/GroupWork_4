import unittest
from selenium import webdriver
from pages_.logInPage import LoginPage


class LogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://us.puma.com/us/en/account/login?action=login")

    def test_positiveLogIn(self):
        logInPageObject = LoginPage(self.driver)
        logInPageObject.fill_username_field("syuzannamuradyan26@gmail.com")
        logInPageObject.click_to_close_cookies_button()
        logInPageObject.fill_password_field("hakob.17")
        logInPageObject.click_to_login_button()
        logInPageObject.validate_network_error_occured_text()

    def tearDown(self):
        self.driver.close()
