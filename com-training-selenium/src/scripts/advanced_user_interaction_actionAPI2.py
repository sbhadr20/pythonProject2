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

    # using Mouse Actions & Keyboard Actions selecting multiple options of a Multi select Element

    driver.get("https://formstone.it/components/dropdown/demo/")
    ele = driver.find_element(By.XPATH, "//select[@id='demo_multiple']")
    driver.execute_script("arguments[0].scrollIntoView();", ele)
    button1 = driver.find_element(By.XPATH, "//select[@id='demo_multiple']/following::div[@class='fs-scrollbar-content']/button[text()='One']")
    button2 = driver.find_element(By.XPATH, "//select[@id='demo_multiple']/following::div[@class='fs-scrollbar-content']/button[text()='Two']")

    time.sleep(3)
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).pause(1).click(button1).pause(1).click(button2).key_up(Keys.CONTROL).perform()
    time.sleep(3)
    webdriver.ActionChains(driver).move_by_offset(0, -20).perform()

    # Close the current tab/window
    driver.close()

except Exception as e:
    print('Exception block ', e)
finally:
    driver.quit()
