from selenium import webdriver
import math
import time

URL = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return math.log(abs(12*math.sin(x)))


try:
    driver = webdriver.Chrome()
    driver.get(URL)
    btn = driver.find_element_by_css_selector("button[type='submit']")
    btn.click()

    first_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    val = driver.find_element_by_css_selector("#input_value").text
    result = calc(int(val))

    input_answer = driver.find_element_by_css_selector("#answer")
    input_answer.send_keys(str(result))

    btn_submit = driver.find_element_by_css_selector("button[type='submit']")
    btn_submit.click()


finally:
    time.sleep(5)
    driver.quit()
