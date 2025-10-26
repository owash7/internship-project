from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

def before_all(context):
    context.config.setup_logging()

    # Read browser and headless flags from Behave userdata
    context.browser_name = context.config.userdata.get("browser", "chrome").lower()
    context.headless = context.config.userdata.get("headless", "false").lower() == "true"

def browser_init(context):
    """
    Initialize browser based on command-line flags
    """
    browser_name = context.browser_name
    headless = context.headless

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

        if headless:
            print("\n** Running Chrome in HEADLESS mode **\n")
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")

        else:
            print("\n** Running Chrome in NORMAL mode **\n")

        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()

        if headless:
            print("\n** Running Firefox in HEADLESS mode **\n")
            options.add_argument("--headless")
        else:
            print("\n** Running Firefox in NORMAL mode **\n")

        # Optional: Set window size explicitly for consistency
        options.set_preference("browser.startup.page", 0)
        options.set_preference("browser.startup.homepage_override.mstone", "ignore")

        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"❌ Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.implicitly_wait(4)
    context.driver = driver
    context.driver.wait = WebDriverWait(driver, 10)
    context.app = Application(driver)

def before_scenario(context, scenario):
    print('\n** Started scenario **:', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\n** Started step **:', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\n❌ Step failed:', step)

def after_scenario(context, feature):
    context.driver.quit()
