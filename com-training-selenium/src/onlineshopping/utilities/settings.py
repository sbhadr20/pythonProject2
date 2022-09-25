import os
from src.onlineshopping.utilities.read_config import ReadConfig


class Settings:
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", ".."))
    home_dir = os.path.expanduser('~')

    url = ReadConfig.url
    username = ReadConfig.username
    password = ReadConfig.password
    platform_name = ReadConfig.platform_name
    browser_name = ReadConfig.browser_name
    browser_version = ReadConfig.browser_version
    screen_resolution = ReadConfig.screen_resolution
    loglevel = ReadConfig.loglevel


if __name__ == '__main__':
    pass
