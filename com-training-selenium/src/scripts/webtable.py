from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")

    # List of elements
    row_elements = driver.find_elements(By.XPATH, "//table[@id='dynamictable']/tr")
    row_count = 0
    for row in row_elements:

        if row_count > 0:
            name = row.find_element(By.XPATH, "td[1]").text
            age = row.find_element(By.XPATH, "td[2]").text
            print("name: "+name+"'s age is: "+age)
        else:
            row_count += 1
            continue

    driver.close()
except Exception as e:
    print('Exception block ', e)
finally:
    driver.quit()
