import json
import os
import configparser

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", ".."))
config_path = os.path.join(root_dir, 'config', 'config.ini')
config = configparser.RawConfigParser()
config.read(config_path)


class ReadConfig:

    url = config.get('credential info', 'url')
    username = config.get('credential info', 'username')
    password = config.get('credential info', 'password')

    platform_name = config.get('test info', 'platformName')
    browser_name = config.get('test info', 'browserName')
    browser_version = config.get('test info', 'browserVersion')
    screen_resolution = config.get('test info', 'screenResolution')

    loglevel = config.get('log info', 'loglevel')
