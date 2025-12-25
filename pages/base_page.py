from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) # this waits upt to 10 seconds

    def find(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        print(f"DEBUG; Type of element is {type(element)}")
        element.send_keys(text)

    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

