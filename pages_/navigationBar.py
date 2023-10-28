from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):

    def click_to_search_field_button(self):
        searchFieldButtonElement = self._find_element(By.XPATH, "//div[@id='nav-bar-sticky']/nav/div/div/button[1]")
        self._click(searchFieldButtonElement)

    def fill_search_field_element(self, text):
        searchFieldElement = self._find_element(By.XPATH, "//input[@name='Search']")
        self._fill_field(searchFieldElement, text)

    def click_to_search_button(self):
        searchButtonElement = self._find_element(By.CSS_SELECTOR, "[data-uds-child='search-form-submit']")
        self._click(searchButtonElement)

    def click_to_add_to_cart_button(self):
        addToCartButtonElement = self.driver.find_element(By.ID, "add-to-cart-button")
        addToCartButtonElement.click()
