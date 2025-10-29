import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from dotenv import load_dotenv

# ✅ Load environment variables from .env file
load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome, firefox, or browserstack")


def before_all(context):
    context.config.setup_logging()
    context.browser_name = context.config.userdata.get("browser", "chrome").lower()
    context.headless = context.config.userdata.get("headless", "false").lower() == "true"


def browser_init(context, scenario_name):
    browser_name = context.browser_name
    headless = context.headless

    # ----------------------------
    # LOCAL BROWSER SETUP
    # ----------------------------
    if browser_name in ["chrome", "firefox"]:
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                print("\n** Running Chrome in HEADLESS mode **\n")
                options.add_argument("--headless=new")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--disable-gpu")
            driver = webdriver.Chrome(options=options)

        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                print("\n** Running Firefox in HEADLESS mode **\n")
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)

    # ----------------------------
    # BROWSERSTACK SETUP
    # ----------------------------
    elif browser_name == "browserstack":
        # ✅ Pull credentials from .env file
        username = os.getenv("BROWSERSTACK_USERNAME")
        access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

        bstack_options = {
            "os": "OS X",
            "osVersion": "Sequoia",  # You can also try "Sonoma" or "Ventura"
            "browserName": "Chrome",
            "browserVersion": "latest",
            "buildName": "Mac BrowserStack Run",
            "projectName": "My Test Project",
            "sessionName": scenario_name,
            "debug": True,
            "networkLogs": True,
            "consoleLogs": "info",
            "userName": username,
            "accessKey": access_key
        }

        options = webdriver.ChromeOptions()
        options.set_capability('bstack:options', bstack_options)

        driver = webdriver.Remote(
            command_executor='https://hub-cloud.browserstack.com/wd/hub',
            options=options
        )

    else:
        raise ValueError(f"❌ Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.implicitly_wait(4)
    context.driver = driver
    context.driver.wait = WebDriverWait(driver, 10)
    context.app = Application(driver)


def before_scenario(context, scenario):
    print('\n** Started scenario **:', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\n** Started step **:', step.name)


def after_step(context, step):
    if step.status == 'failed':
        print(f'\n❌ Step failed: {step.name}')


def after_scenario(context, scenario):
    print(f'\n** Finished scenario: {scenario.name} **')
    context.driver.quit()
