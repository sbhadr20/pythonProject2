from src.onlineshopping.utilities.browser_session import BrowserSession
from src.onlineshopping.utilities.settings import Settings
from src.onlineshopping.utilities.create_screenshot_structure import CreateScreenshotStructure
from src.onlineshopping.pages.login_page import LoginPage
import pytest


@pytest.fixture()
def setup_driver():
    CreateScreenshotStructure.create_ss_folder()
    driver = BrowserSession.create_browser_session()
    driver.get(Settings.url)
    return driver


@pytest.fixture()
def setup_login_page(setup_driver):
    login = LoginPage(setup_driver)
    return login
