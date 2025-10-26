import re
from pages.base_page import Page
from selenium.webdriver.common.by import By

class SideMenu(Page):
    SIDE_MENU = (By.CSS_SELECTOR, "div[id*='w-node']")
    OFF_PLAN_BTN = (By.XPATH, "//div[contains(@class,'menu-text')"
                                "and text()='Off-plan']")
    OFF_PLAN_TXT = (By.CSS_SELECTOR, "button[class*='pb-5']")
    PRICE_FILTER_DD = (By.CSS_SELECTOR, "button[data-test-id='filter-price-dropdown']")
    MIN_PRICE = (By.CSS_SELECTOR, "input[id*='priceMin']")
    MAX_PRICE = (By.CSS_SELECTOR, "input[id*='priceMax']")
    APPLY_FILTER = (By.XPATH, "//button[text()='Apply filter']")
    CARD_PRICE = (By.CSS_SELECTOR, "h5[class*='text-sm']")


    def click_off_plan_btn(self):
        # self.wait_for_element_visible(*self.SIDE_MENU)
        self.wait_for_element_clickable_click(*self.OFF_PLAN_BTN)

    def verify_off_plan_txt(self):
        self.wait_for_element_visible(*self.OFF_PLAN_TXT)
        self.verify_text("Off-plan", *self.OFF_PLAN_TXT)

    def click_price_filter_btn(self):
        self.wait_for_element_visible(*self.PRICE_FILTER_DD)
        self.click(*self.PRICE_FILTER_DD)

    def input_min_price(self, min_price):
        self.wait_for_element_visible(*self.MIN_PRICE)
        self.input_text(min_price, *self.MIN_PRICE)

    def input_max_price(self, max_price):
        self.input_text(max_price, *self.MAX_PRICE)

    def click_apply_filter_btn(self):
        self.click(*self.APPLY_FILTER)


# This code will go through the different outputs of the price range entered and return a list whether they are in range or not
    # def verify_price_in_range(self, min_price, max_price):
    #     print(f"Checking prices between {min_price} and {max_price} AED\n")
    #
    #     price_elements = self.driver.find_elements(*self.CARD_PRICE)
    #     print(f"Found {len(price_elements)} property price elements\n")
    #
    #     for index, card in enumerate(price_elements, start=1):
    #         text = card.text.strip()
    #         match = re.search(r"(\d[\d\s,]*)\s?AED", text)
    #         if match:
    #             num_str = match.group(1).replace(" ", "").replace(",", "")
    #             try:
    #                 price = int(num_str)
    #                 if int(min_price) <= int(price) <= int(max_price):
    #                     print(f"{index}. {price:,} AED ✅ In range")
    #                 else:
    #                     print(f"{index}. {price:,} AED ❌ Out of range")
    #             except ValueError:
    #                 print(f"{index}. Could not parse number from: {text}")

# This code will through an assert message if a product is out of range and fail the test
    def verify_price_in_range(self, min_price, max_price):
        price_elements = self.find_elements(*self.CARD_PRICE)
        min_price = int(min_price)
        max_price = int(max_price)

        for index, element in enumerate(price_elements, start=1):
            text = element.text.strip()
            match = re.search(r"(\d[\d\s,]*)\s?AED", text)

            if match:
                # Clean and convert to integer (remove commas/spaces)
                price = int(match.group(1).replace(",", "").replace(" ", ""))

                # Assertion for in-range validation
                assert min_price <= price <= max_price, (
                    f"❌ {index}. Price {price:,} AED is OUT of range "
                    f"({min_price:,} - {max_price:,})"
                )

                print(f"✅ {index}. {price:,} AED is within range.")
            else:
                print(f"⚠️ {index}. No valid price text found → '{text}'")
