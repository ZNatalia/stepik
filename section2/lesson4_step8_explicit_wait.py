from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

URL = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    driver = webdriver.Chrome()
    driver.get(URL)
    # Wait until the price in the title is $100
    title_price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )

    btn_book = driver.find_element_by_css_selector("button#book")
    btn_book.click()

    val = driver.find_element_by_css_selector("#input_value").text
    result = calc(int(val))
    input_answer = driver.find_element_by_css_selector("#answer")
    input_answer.send_keys(str(result))
    #
    btn_solve = driver.find_element_by_css_selector("#solve")
    btn_solve.click()

finally:
    time.sleep(5)
    driver.quit()


