import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

try:
    driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
    driver.implicitly_wait(5)
    # to maximize the window
    driver.maximize_window()
    driver.get("https://www.selenium.dev/documentation/webdriver/browser/alerts/")  # Or

    # driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

    # ********* Click the link to activate the alert *************
    driver.find_element(By.LINK_TEXT, "See an example alert").click()
    # Wait for the alert to be displayed and store it in a variable
    alert = WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
    # Store the alert text in a variable
    text = alert.text
    # Press the OK button
    alert.accept()

    # *********** Click the link to activate the CONFIRM **************
    driver.find_element(By.LINK_TEXT, "See a sample confirm").click()
    # Wait for the alert to be displayed
    WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
    # Store the alert in a variable for reuse
    alert = driver.switch_to.alert
    # Store the alert text in a variable
    text = alert.text
    # Press the Cancel button
    alert.dismiss()
    # alert.accept()

    # *********** Click the link to activate the Prompt ************
    driver.find_element(By.LINK_TEXT, "See a sample prompt").click()
    # Wait for the alert to be displayed
    WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
    # Store the alert in a variable for reuse
    alert = Alert(driver)
    # Type your message
    alert.send_keys("Selenium")
    # Press the OK button
    alert.accept()

except Exception as e:
    print('Exception block ', e)
finally:
    driver.quit()
