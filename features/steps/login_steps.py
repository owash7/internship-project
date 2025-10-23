from behave import given, then, when
from config import Config


@given("User navigates to login page")
def navigate_to_login_page(context):
    context.app.login_page.open_login()

@then("User inputs email")
def input_email(context):
    context.app.login_page.enter_email(Config.EMAIL)

@then("User inputs password")
def input_password(context):
    context.app.login_page.enter_password(Config.PASSWORD)

@when("User clicks continue button")
def click_login_btn(context):
    context.app.login_page.click_continue_btn()

@then("Home screen is presented")
def home_screen(context):
    context.app.login_page.verify_home_url()

@then("Complete login")
def complete_login(context):
    context.app.login_page.complete_login(Config.EMAIL, Config.PASSWORD)