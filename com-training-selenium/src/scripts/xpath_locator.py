import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

try:
    driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@class='submit-button btn_action']").click()

    fluent_wait = WebDriverWait(driver, 20, poll_frequency=5, ignored_exceptions=[ElementNotVisibleException])
    link_element = fluent_wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='header_secondary_container']/span[text()='Products']")))
    assert("Element should be displayed: ", link_element.is_displayed())

    products = ['Sauce Labs Backpack', 'Sauce Labs Bike Light']
    total_price = 0
    for product in products:
        price = driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='"+product+"']/../../following-sibling::div/div").text
        driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='"+product+"']/following::button[1]").click()         # by index position
        # driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']/../../following-sibling::div/button[text()='Add to cart']").click()
        price = price[1:]
        total_price = total_price+float(price)

    print("Added all products to the Cart, total price is: $"+str(total_price))
    time.sleep(5)
    driver.close()
except Exception as e:
    print('Exception block '+e)
finally:
    driver.quit()
