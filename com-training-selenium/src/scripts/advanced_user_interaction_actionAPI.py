import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


try:
    driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
    driver.implicitly_wait(10)
    # to maximize the window
    driver.maximize_window()
    driver.get("https://crossbrowsertesting.github.io/")

    # Mouse Actions
    # driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
    #
    # element1 = driver.find_element(By.ID, "draggable")
    # element2 = driver.find_element(By.ID, "droppable")
    # webdriver.ActionChains(driver).click_and_hold(element1).move_to_element(element2).release().perform()

    # Drag and Drop
    driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
    element1 = driver.find_element(By.ID, "draggable")
    element2 = driver.find_element(By.ID, "droppable")
    time.sleep(3)
    webdriver.ActionChains(driver).drag_and_drop(element1, element2).perform()

    # move_to_element
    driver.back()
    driver.find_element(By.LINK_TEXT, "Hover Menu").click()
    element = driver.find_element(By.CLASS_NAME, "dropdown")
    time.sleep(3)
    action = ActionChains(driver).move_to_element(element).perform()

    time.sleep(5)
    # Close the current tab/window
    driver.close()


except Exception as e:
    print('Exception block ', e)
finally:
    driver.quit()
