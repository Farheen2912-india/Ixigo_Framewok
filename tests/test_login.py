import pytest
from Ixigo_Login_Framework.pages.login_page import LoginPage
from Ixigo_Login_Framework.utilities.read_excel import get_data

@pytest.mark.parametrize("email,password", get_data())
def test_google_login(driver, email, password):
    login = LoginPage(driver)

    login.click_login_signup()
    login.click_google_button()
    login.enter_email(email)
    login.click_email_next()
    login.enter_password(password)
    login.click_password_next()

