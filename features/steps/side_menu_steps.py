from behave import given, then, when

@then("User clicks off-plan in side menu")
def user_click_off_plan_btn(context):
    context.app.side_menu.click_off_plan_btn()

@then("User verifies they are on Off-plan page")
def user_verifies_off_plan_btn(context):
    context.app.side_menu.verify_off_plan_txt()

@when("User clicks the Price filter")
def user_click_price_filter_btn(context):
    context.app.side_menu.click_price_filter_btn()

@then("User inputs the {min_price} and {max_price}")
def user_inputs_price(context, min_price, max_price):
    context.app.side_menu.input_min_price(min_price)
    context.app.side_menu.input_max_price(max_price)

@then("User clicks the apply filter button")
def user_click_apply_filter_btn(context):
    context.app.side_menu.click_apply_filter_btn()

@then("User verifies all visible property prices are within range {min_price} and {max_price}")
def verify_all_prices_in_range(context, min_price, max_price):
    context.app.side_menu.verify_price_in_range(min_price, max_price)
