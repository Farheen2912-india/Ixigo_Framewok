from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Ixigo_Login_Framework.pages.base_page import BasePage

class LoginPage(BasePage):
    login_signup = (By.XPATH,"(//button[contains(.,'Log in/Sign up')])[1]")
    google_login = (By.XPATH,"//*[contains(text(),'Sign in with Google')]")
    email = (By.ID,"identifierId")
    email_next = (By.XPATH,"//span[text()='Next']")
    password_txt = (By.NAME,"Passwd")
    password_next = (By.XPATH,"//span[text()='Next']")

    def __init__(self, driver):
        super().__init__(driver)
        self.parent_window = None  #only one browser window

    def click_login_signup(self):
        self.click(self.login_signup)

    def click_google_button(self):
        self.parent_window = self.driver.current_window_handle #selenium knows which is parent window

        # Wait for the Google button
        element = self.wait.until(EC.presence_of_element_located(self.google_login)) #wait until google button appears

        # Scroll to the element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element) #Scroll until it becomes visible

        # JavaScript click
        self.driver.execute_script("arguments[0].click();", element)  # JS click

        # Wait for Google window to open
        self.wait.until(lambda d: len(d.window_handles) > 1) #Wait until Google window opens.

        # Switch to Google window
        for window in self.driver.window_handles:  # loop through every window
            if window != self.parent_window:        #Ignore parent window
                self.driver.switch_to.window(window)  #Switch Selenium control to Google Login page.
                break
                
    def enter_email(self, email):
        self.enter_text(self.email, email)

    def click_email_next(self):
        self.click(self.email_next)

    def enter_password(self, password):
        self.enter_text(self.password_txt, password)

    def click_password_next(self):
        self.click(self.password_next)

