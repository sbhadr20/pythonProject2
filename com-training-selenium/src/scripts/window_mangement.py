import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
# from selenium.webdriver.support.relative_locator import locate_with


try:
    driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
    driver.implicitly_wait(5)
    # to maximize the window
    # driver.maximize_window() //driver.fullscreen_window()
    driver.get("https://crossbrowsertesting.github.io/")

    driver.find_element(By.LINK_TEXT, 'Login Form').click()
    # username_element = driver.find_element(locate_with(By.TAG_NAME, "input").above({By.ID: "password"}))

    size = driver.get_window_size()
    height = size.get("height")
    width = size.get("width")
    print("width X Height of the window ", width, height)
    driver.set_window_size(width-50, height-50)
    size = driver.get_window_size()
    height = size.get("height")
    width = size.get("width")
    print("Modified width X Height of the window ", width, height)
    driver.maximize_window()
    position = driver.get_window_position()
    x = position.get("x")
    y = position.get("y")
    print("x,y coordinates of the window ", x, y)

    driver.set_window_position(x+10, y+10)
    position = driver.get_window_position()
    x = position.get("x")
    y = position.get("y")
    print("x,y coordinates of the window ", x, y)

    # driver.find_element(By.LINK_TEXT, 'Login Form').click()
    rectangle = driver.find_element(By.ID, 'username').rect
    print('height', rectangle['height'])
    print('width', rectangle['width'])
    print('x', rectangle['x'])
    print('y', rectangle['y'])

    # driver.find_element(By.LINK_TEXT, 'Login Form').click()
    fore_ground_color = driver.find_element(By.ID, 'submit').value_of_css_property('color')
    expected_fg_color = Color.from_string('rgb(255, 255, 255)')
    assert expected_fg_color == fore_ground_color, 'validation of color attribute'
    print('fore_ground_color', fore_ground_color)

except Exception as e:
    print('Exception block ', e)
finally:
    driver.quit()
