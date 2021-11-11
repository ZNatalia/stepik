from selenium import webdriver
import math
import time

url = "http://suninjuly.github.io/execute_script.html"

def calc(x):

    return math.log(abs(12 * math.sin(x)))

try:
    driver = webdriver.Chrome()
    driver.get(url)
    number = driver.find_element_by_css_selector("#input_value").text
    result_of_calc = calc(float(number))
    # Insert result_of_calc
    input_answer = driver.find_element_by_css_selector("#answer")
    input_answer.send_keys(str(result_of_calc))

    # Scroll the web page
    button = driver.find_element_by_tag_name("button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Check checkbox
    check_box = driver.find_element_by_css_selector("[for='robotCheckbox']")
    check_box.click()

    # Switch radio btn
    radio_btn = driver.find_element_by_css_selector("[for='robotsRule']")
    radio_btn.click()

    # Click the submit button
    button.click()


finally:
    time.sleep(5)
    driver.quit()
