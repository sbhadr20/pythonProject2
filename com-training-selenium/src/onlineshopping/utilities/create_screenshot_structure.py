import os
from src.onlineshopping.utilities.settings import Settings
from shutil import rmtree


class CreateScreenshotStructure:

    TestNameIt = 0
    current_screen_path = os.path.join(Settings.root_dir,'screenshots')

    @staticmethod
    def create_folder(name):
        try:
            CreateScreenshotStructure.TestNameIt = CreateScreenshotStructure.TestNameIt +1 ;
            path = os.path.join(CreateScreenshotStructure.current_screen_path,name)
            if not os.path.exists(path):
                os.makedirs(path)
            return path
        except OSError:
            print('Error: creating directory ')

    @staticmethod
    def create_ss_folder():
        try:
            path = CreateScreenshotStructure.current_screen_path
            if os.path.exists(path):
                rmtree(path)
            os.makedirs(path)
        except OSError:
            print('Error: creating directory '+path)