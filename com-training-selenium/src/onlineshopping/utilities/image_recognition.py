import time
import os
from src.onlineshopping.utilities.settings import Settings


class ImageRecognition:

    driver=None
    counter = 1

    def __init__(self, driver):
        print("ImageRecognition init....")
        self.driver=driver

    def get_current_screen(self):
        try:
            current_screen_path = os.path.join(Settings.root_dir,'screenshots','CurrentScreen.png')
            self.driver.get_screenshot_as_file(current_screen_path)
            return current_screen_path
        except Exception as e:
            print('Exception block ')
            return None

    def get_screenshot(self, name):
        try:
            path = os.path.join(self.current_test_screenshot_path, str(ImageRecognition.counter)+'-'+name+'.png')
            time.sleep(1)
            print('path', path)
            self.driver.get_screenshot_as_file(path)
            ImageRecognition.counter = ImageRecognition.counter+1
            print('ImageRecognition.counter '+str(ImageRecognition.counter))
        except Exception as e:
            print('Exception block ')

    def get_step_screenshot(self, name):
        try:
            path = os.path.join(self.current_test_screenshot_path, str(ImageRecognition.counter)+'-'+name+'.png')
            time.sleep(1)
            print('path', path)
            self.driver.save_screenshot(path)
            ImageRecognition.counter = ImageRecognition.counter+1
            print('ImageRecognition.counter '+str(ImageRecognition.counter))
        except Exception as e:
            print('Exception block ')
