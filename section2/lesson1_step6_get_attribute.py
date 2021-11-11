from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

url = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:

    browser = webdriver.Chrome()
    browser.get(url)

    # Find the image
    treasure_img = browser.find_element_by_css_selector("#treasure")
    # Get the value of the attribute of the image
    x = int(treasure_img.get_attribute("valuex"))
    result = calc(x)
    print(result)

    # Find and insert the value got from image attribute in the input field
    input_answer = browser.find_element_by_css_selector("#answer")

    input_answer.send_keys(result)

    # Find the checkbox el and check it
    check_robot = browser.find_element_by_css_selector("#robotCheckbox")
    check_robot.click()

    # Find radio el and choose it
    radio_robotos = browser.find_element_by_css_selector("#robotsRule")
    radio_robotos.click()

    #Find the submit button and click it

    submit_btn = browser.find_element_by_css_selector("[type = 'submit']")
    submit_btn.click()



finally:
    time.sleep(5)
    browser.quit()
