import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def navigate_to_child_window(driver, parent_window, service_type, expected_title):
    element = driver.find_element(By.XPATH, "//*[normalize-space(text()) = '" + service_type + "']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[contains(text(),'" + service_type + "')]/parent::h2/following::a[1]").click()
    for windowHandle in driver.window_handles:
        driver.switch_to.window(windowHandle)
        get_current_title = driver.title
        if get_current_title == expected_title:
            break

try:
    driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
    driver.implicitly_wait(20)

    # to maximize the window
    driver.maximize_window()
    driver.get("https://www.cigniti.com/")

    # to click on the hyperlink to accept cookies
    driver.find_element(By.XPATH, "//button[contains(text(),'OK, Got It!')]").click()

    # Store the ID of the original window
    parent_window = driver.current_window_handle
    driver.find_element(By.XPATH, "//a[text() = 'Digital Assurance'][1]").click()

    expected_title = "Software Quality Engineering & Testing Services | QA Consulting Company"
    navigate_to_child_window(driver, parent_window, "Quality Engineering Services", expected_title)
    childWindowTitleFinalPage = "Test Automation Services | QA Automation Services Company"

    # to click on the hyperlink
    driver.find_element(By.XPATH, "//a/strong[normalize-space(text())='Test Automation']").click()
    print("Navigated to the Page ? : ", childWindowTitleFinalPage == driver.title)
    print("Navigated to the Page ? : ", driver.current_url)

    # Close the current tab/window
    driver.close()

    # Switch back to the parent window
    driver.switch_to.window(parent_window)
    expected_title = "Digital Assurance & Testing Services | Digital Transformation Solutions"
    navigate_to_child_window(driver, parent_window, "Digital Assurance Services", expected_title)

except Exception as e:
    print('Exception block ', e)
finally:
    driver.quit()
