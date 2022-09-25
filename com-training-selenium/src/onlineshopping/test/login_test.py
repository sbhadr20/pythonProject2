import pytest
from src.onlineshopping.utilities.settings import Settings
from src.onlineshopping.utilities.custom_logger import CustomLog
from src.onlineshopping.utilities.read_config import ReadConfig


class TestLoginValidations:
    logger = CustomLog.log()

    @pytest.mark.positive
    def test_login_pass(self, setup_driver, setup_login_page):
        self.logger.info("Begin")
        self.driver = setup_driver
        self.login = setup_login_page
        self.login.enter_username(Settings.username)
        self.login.enter_password(Settings.password)
        self.logger.debug("User: "+Settings.username)
        self.login.click_login()
        self.driver.quit()
        self.logger.info("End")

    @pytest.mark.negative
    def test_login_pass2(self, setup_driver, setup_login_page):
        self.logger.info("Begin")
        self.driver = setup_driver
        self.login = setup_login_page
        self.login.enter_username(Settings.username)
        self.login.enter_password(Settings.password)
        self.login.click_login()
        self.driver.quit()
        self.logger.info("End")
