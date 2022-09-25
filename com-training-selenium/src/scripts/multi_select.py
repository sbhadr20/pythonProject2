from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome(executable_path="../../resources/drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
    select_element = driver.find_element(By.XPATH, "//select[@name='selenium_commands']")
    driver.execute_script("arguments[0].scrollIntoView();", select_element)
    select_object = Select(select_element)
    select_object.select_by_visible_text('Navigation Commands')
    select_object.select_by_visible_text('Switch Commands')

    """
    driver.get("https://formstone.it/components/dropdown/demo/")

    # Handle Multi-select Dropdown list

    select_element = driver.find_element(By.XPATH, "//select[@id='demo_multiple']")
    driver.execute_script("arguments[0].scrollIntoView();", select_element)
    select_object = Select(select_element)

    # Return a list[WebElement] of options that the <select> element contains
    all_available_options = select_object.options

    # some <select> elements allow you to select more than one option.
    does_this_allow_multiple_selections = select_object.is_multiple

    # select_object.select_by_index(1)
    # select_object.select_by_index(2)

    # Select an <option> based upon its text
    select_object.select_by_visible_text('One')
    select_object.select_by_visible_text('Two')

    # Return a list[WebElement] of options that have been selected
    if does_this_allow_multiple_selections:
        all_selected_options = select_object.all_selected_options

    # Deselect an <option> based upon its textif does_this_allow_multiple_selections:
    if does_this_allow_multiple_selections:
        select_object.deselect_by_visible_text('Two')

    # Deselect an <option> based upon the <select> element's internal index
    # if does_this_allow_multiple_selections:
    #     select_object.deselect_by_index(1)

    # Deselect an <option> based upon its value attribute
    # if does_this_allow_multiple_selections:
    #     select_object.deselect_by_value('2')

    # Return a WebElement referencing the first selection option found by walking down the DOM
    # first_selected_option = select_object.first_selected_option

    # Deselect all selected <option> elements
    if does_this_allow_multiple_selections:
        select_object.deselect_all()
    """

    driver.close()
except Exception as e:
    print('Exception block ', e)
finally:
    driver.quit()
