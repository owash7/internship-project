from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SettingsPage(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, "a[href='/settings']")
    MY_CLIENTS_BTN = (By.CSS_SELECTOR, "a[href='/my-fixations']")
    OPTIONS_BTN = (By.CSS_SELECTOR, "div[w-el-class='tag-properties']")
    CLIENT_MODE = (By.CSS_SELECTOR, "div[class*='page-setting-block']")
    SETTINGS_OPTIONS = (By.CSS_SELECTOR, "a[class*='page-setting-block']")
    CONNECT_COMPANY_BTN = (By.XPATH, "//div[text()='Connect the company']")

    def click_settings(self):
        self.wait_for_element_clickable_click(*self.SETTINGS_BTN)

    def click_my_clients(self):
        self.wait_for_element_clickable_click(*self.MY_CLIENTS_BTN)

    def verify_my_fixations_page(self):
        self.verify_partial_url("my-fixations")

    def verify_settings_page(self):
        self.verify_partial_url("settings")

    def verify_option_amount(self, number):
        self.verify_element_count(7, *self.OPTIONS_BTN)

    def verify_settings_options_amount(self, expected_number):
         client_mode_element = self.find_elements(*self.CLIENT_MODE)
         settings_options_elements = self.find_elements(*self.SETTINGS_OPTIONS)
         total_amount = len(client_mode_element) + len(settings_options_elements)
         expected_number = int(expected_number)
         assert total_amount == expected_number, f'Expected {expected_number}, but got {total_amount}'

    def connect_the_company_btn(self):
        self.find_element(*self.CONNECT_COMPANY_BTN)




