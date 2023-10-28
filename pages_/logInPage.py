from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class LoginPage(BasePage):


    def fill_username_field(self, username):
        usernameFieldElement = self._find_element(By.ID, "email")
        self._fill_field(usernameFieldElement, username)

    def fill_password_field(self, password):
        paswordFieldElement = self._find_element(By.ID, "password")
        self._fill_field(paswordFieldElement, password)

    def click_to_close_cookies_button(self):
        closeCookiesButtonElement=self._find_element(By.CSS_SELECTOR, "[data-test-id='cookie-banner-close-btn']")
        self._click(closeCookiesButtonElement)

    def click_to_login_button(self):
        loginButtonElement = self._find_element(By.ID, "login-submit")
        self._click(loginButtonElement)

    def validate_network_error_occured_text(self):
        networkErrorOccuredElement=self._find_element(By.CSS_SELECTOR, "[data-test-id='login-form-error']")
        if self._get_text(networkErrorOccuredElement) != "A network error occurred":
            print("Error: Wrong network issue.")
            exit(2)

