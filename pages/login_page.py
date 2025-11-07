from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage(Page):
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[class*='login-button']")

    def open_login(self):
        self.open_url("https://soft.reelly.io/sign-in")

    def enter_email(self, email):
        self.wait_for_element_visible(*self.EMAIL_FIELD)
        self.input_text(email, *self.EMAIL_FIELD)

    def enter_password(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_continue_btn(self):
        self.click(*self.LOGIN_BUTTON)
        sleep(2)

    def verify_home_url(self):
        self.verify_url("https://soft.reelly.io/")
        sleep(2)

    def complete_login(self,email,password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_continue_btn()
