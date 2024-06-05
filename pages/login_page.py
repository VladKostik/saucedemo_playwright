import os
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = os.getenv("SAUCEDEMO_URL")
        self.username_input = "//input[@data-test='username']"
        self.password_input = "//input[@data-test='password']"
        self.login_button = "//input[@data-test='login-button']"
        self.epic_sadface = '//h3[@data-test="error"]'

    def load(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_error_message_visible(self):
        return self.is_element_visible(self.epic_sadface)

    def get_error_mess_text(self):
        return self.get_element_text(self.epic_sadface)
