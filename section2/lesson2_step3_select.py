from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


url = "http://suninjuly.github.io/selects1.html"
try:
    driver = webdriver.Chrome()
    driver.get(url)

    # Find the number1
    first_number = driver.find_element_by_css_selector("#num1").text

    # Find the number2
    second_number = driver.find_element_by_css_selector("#num2").text

    # Find the sum of the number1 and number2
    sum_numbers = int(first_number) + int(second_number)

    # Find the dropdown

    select = Select(driver.find_element_by_css_selector("#dropdown"))

    # Select option by value
    select.select_by_value(str(sum_numbers))

    # Click the submit button
    driver.find_element_by_css_selector("button[type='submit']").click()

finally:
    time.sleep(5)
    driver.quit()
