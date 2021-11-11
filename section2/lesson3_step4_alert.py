from selenium import webdriver
import math
import time

URL = "http://suninjuly.github.io/alert_accept.html"


def calc(x):

    return math.log(abs(12 * math.sin(x)))
try:
    driver = webdriver.Chrome()
    driver.get(URL)
    # Click the button "I want to go"
    btn_submit = driver.find_element_by_css_selector("[type='submit']")
    btn_submit.click()
    alert = driver.switch_to.alert
    alert.accept()

    # Calculate
    val = driver.find_element_by_css_selector("#input_value").text
    result_calc = calc(int(val))

    # Find input field
    input_answer = driver.find_element_by_css_selector("#answer")
    # Input the result of calculation
    input_answer.send_keys(str(result_calc))

    # Find the button Submit

    btn_submit = driver.find_element_by_css_selector("button[type='submit']")
    btn_submit.click()

finally:
    time.sleep(5)
    driver.quit()