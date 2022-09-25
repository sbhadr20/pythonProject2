from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://pypi.org/")

    # Handle Input/Text box
    search_input = driver.find_element(By.ID, "search")     # To store an element reference
    search_input.clear()                              # To clear the text from input box
    search_input.send_keys("selenium")      # To input the text onto input box
    enteredText = search_input.get_attribute('value')    # To retrieve the text from input box

    driver.find_element(By.CLASS_NAME, "search-form__button").click()

    # Handle Dropdown list
    select_element = driver.find_element(By.ID, 'order')
    select_object = Select(select_element)

    # Return a list[WebElement] of options that the <select> element contains
    all_available_options = select_object.options

    # Select an <option> based upon its text
    select_object.select_by_visible_text('Trending')

    # Select an <option> based upon its value attribute
    # select_object.select_by_value('-zscore')

    # Handle Links.
    link_element = driver.find_element(By.PARTIAL_LINK_TEXT, 'selenium')
    link_element.click()

    link_login = driver.find_element(By.LINK_TEXT, 'Log in')
    link_login.click()

    driver.find_element(By.ID,'username').send_keys("userA")
    driver.find_element(By.ID, 'password').send_keys("pswd")

    # Handle Button
    button_login = driver.find_element(By.XPATH, "//input[@type='submit']")
    if button_login.is_enabled():
        button_login.click()

    # Handle Checkbox
    checkbox_element = driver.find_element(By.ID, "show-password")
    # checkbox_element.is_selected()
    checkbox_element.click()
    driver.close()
except Exception as e:
    print('Exception block '. e)
finally:
    driver.quit()
