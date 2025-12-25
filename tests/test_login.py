import os

from pages.login_page import LoginPage
import pytest
from dotenv import  load_dotenv
load_dotenv()

PASSWORD = os.getenv("SAUCE_PASSWORD")


'''
def test_valid_login(driver):
    username = "standard_user"
    password = "secret_sauce"
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)
    assert "inventory.html" in driver.current_url, "Login Failed or redirected to wrong page"

'''


@pytest.mark.parametrize ("user, password", [
    ("standard_user", PASSWORD),      # Valid User
    ("locked_out_user", PASSWORD),   # Invalid User (Should fail)
    ("problem_user", PASSWORD)        # Glitchy User
])


def test_multiple_login(driver,user,password,should_pass):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username=user ,password=password)
    assert  "inventory.html" in driver.current_url

    if should_pass:
        assert "inventory.html" in driver.current_url
    else:
        error_text = login_page.get_error_message()
        assert "locked out" in error_text.lower()
        print(f"Captured expected error:{error_text}")