from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://pypi.org/")

    # Handle Input/Text box
    search_input = driver.find_element(By.CSS_SELECTOR, "#search")    # To store an element reference
    search_input.send_keys("selenium")                          # To input the text onto input box
    enteredText = search_input.get_attribute('value')           # To retrieve the text from input box
    print("enteredText", enteredText)

    # Click on Search Icon
    driver.find_element(By.CSS_SELECTOR, "button.search-form__button").click()    # or

    # driver.find_element(By.CSS_SELECTOR, "#search + button").click()
    # driver.find_element(By.CSS_SELECTOR, "label[for='search'] ~ button").click()

    # Handle Dropdown list
    select_element = driver.find_element(By.CSS_SELECTOR, "select[id='order']")
    select_element.click()
    # select_object = Select(select_element)

    # Select an <option> based upon its text
    # index starts from 1
    driver.find_element(By.CSS_SELECTOR, "#order option:nth-of-type(2)").click()

    # Handle Links.
    link_element = driver.find_element(By.CSS_SELECTOR, ".package-snippet")
    link_element.click()

    link_help = driver.find_element(By.CSS_SELECTOR, "ul > li[class='horizontal-menu__item']:nth-of-type(2)")
    link_help.click()

    # Handle Button
    button_login = driver.find_element(By.CSS_SELECTOR, "a[href$='login/']")
    button_login.click()

    # Handle Checkbox
    checkbox_element = driver.find_element(By.CSS_SELECTOR, "input[id='show-password'][type='checkbox']")
    checkbox_element.click()

    driver.close()
except Exception as e:
    print('Exception block '. e)
finally:
    driver.quit()
