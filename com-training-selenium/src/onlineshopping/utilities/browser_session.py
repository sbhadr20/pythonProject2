import os
from selenium import webdriver
from src.onlineshopping.utilities.settings import Settings


class BrowserSession:

    device_width = None
    device_height = None
    driver = None

    @staticmethod
    def create_browser_session():
        try:
            print("creation")
            driver_path = os.path.join(Settings.root_dir,'resources','drivers')
            if Settings.browser_name.upper() == 'CHROME':
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--disable-notifications")
                chrome_options.add_argument("--disable-popup-blocking")
                chrome_options.add_argument("--start-maximized")
                chrome_path = driver_path+"/chromedriver.exe"
                driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
            else:
                print('You have not chosen Chrome Browser !')
            print("session initialization....")
            screen_resolution = Settings.screen_resolution.split('x')
            driver.set_window_size(screen_resolution[0], screen_resolution[1])
            window_size = driver.get_window_size()
            BrowserSession.device_width = window_size['width']
            BrowserSession.device_height = window_size['height']            
            driver.implicitly_wait(5)
        except:
            print('Exception occurred during selenium driver instantiation !')
            exit(0)
        finally:
            config = None
            return driver


if __name__ == '__main__':
    pass