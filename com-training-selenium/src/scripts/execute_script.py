import time
from selenium.webdriver.common.by import By
from selenium import webdriver


try:
    driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
    driver.implicitly_wait(10)
    # to maximize the window
    driver.maximize_window()
    # driver.get("https://www.google.com/")
    # element = driver.find_element(By.NAME, "q")
    # driver.execute_script("arguments[0].value='selenium';", element)
    #
    # element2 = driver.find_element(By.NAME, "btnK")
    # driver.execute_script("arguments[0].click();", element2)

    driver.get("https://pypi.org/")
    driver.execute_script('document.getElementsByClassName("search-form__search large-input")[0].value=\'selenium\'')
    driver.execute_script('document.getElementsByClassName("search-form__button")[0].click()')

    # Close the current tab/window
    driver.close()


except Exception as e:
    print('Exception block ', e)
finally:
    driver.quit()
