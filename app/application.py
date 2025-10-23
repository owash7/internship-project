from pages.base_page import Page
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.side_menu import SideMenu

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(driver)
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
        self.side_menu = SideMenu(driver)


