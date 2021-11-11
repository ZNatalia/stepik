from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x = browser.find_element_by_css_selector(".form-group span#input_value").text
    result = calc(x)

    input_answer = browser.find_element_by_css_selector("input#answer")
    input_answer.send_keys(result)

    checkbox_robot = browser.find_element_by_css_selector("[for = 'robotCheckbox']")
    checkbox_robot.click()

    radio_btn = browser.find_element_by_css_selector("[for=robotsRule]")
    radio_btn.click()

    btn_submit = browser.find_element_by_css_selector("button[type='submit']")
    btn_submit.click()


finally:
    time.sleep(10)
    browser.quit()


