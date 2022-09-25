from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions


driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://pypi.org/")
link_login = driver.find_element(By.LINK_TEXT, 'Log in')
link_login.click()

page_title = driver.find_element(By.CLASS_NAME, "page-title").is_displayed()
if page_title:
    driver.find_element(By.ID, 'username').send_keys("userA")
    driver.find_element(By.ID, 'password').send_keys("Pswd")
    checkbox_element = driver.find_element(By.ID,"show-password")
    is_element_checked = checkbox_element.is_selected()
    if not is_element_checked:
        checkbox_element.click()
    submit_element = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
    submit_element.click()

driver.close()
print("End of the session")
driver.quit()
