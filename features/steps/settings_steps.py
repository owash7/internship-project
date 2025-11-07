from behave import given, then, when

@then("Click settings button")
def click_settings(context):
    context.app.settings_page.click_settings()

@then("Click My clients button")
def click_my_clients(context):
    context.app.settings_page.click_my_clients()

@then("Verify correct page opened")
def verify_correct_page(context):
    context.app.settings_page.verify_my_fixations_page()

@then("Verify settings page opened")
def verify_settings_page(context):
    context.app.settings_page.verify_settings_page()

@then("Verify the option amount on the page is {number}")
def verify_option_amount(context, number):
    context.app.settings_page.verify_option_amount(number)

@then("Verify the amount of options is {amount}")
def verify_settings_options_amount(context, amount):
    context.app.settings_page.verify_settings_options_amount(amount)

@then("Verify connect the company button is available")
def verify_company_button(context):
    context.app.settings_page.connect_the_company_btn()