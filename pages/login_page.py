from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    Username_filed = (By.ID,"user-name")
    password_field = (By.ID,"password")
    login_button = (By.ID,"login-button")

    def __init__(self,driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    def load(self):
        self.driver.get(self.url)

    def login(self,username,password):
        self.type(self.Username_filed,username)
        self.type(self.password_field,password)
        self.click(self.login_button)

    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def get_error_message(self):
        return self.find(self.ERROR_MESSAGE).text



