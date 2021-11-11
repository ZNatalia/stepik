import os

from selenium import webdriver
import time

url = "http://suninjuly.github.io/file_input.html"
try:
    driver = webdriver.Chrome()
    driver.get(url)

    # Input the first name
    input_first_name = driver.find_element_by_css_selector("input[name='firstname']")
    input_first_name.send_keys("Natalia")

    # Input the last name
    input_last_name = driver.find_element_by_css_selector("input[name='lastname']")
    input_last_name.send_keys("Li")

    # Input an email
    input_email = driver.find_element_by_css_selector("input[name='email']")
    input_email.send_keys("bnnm@gmail.com")

    # Define the current dir
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Define the path of text document
    file_path = os.path.join(current_dir, 'test.txt')
    # Find the choose_file button
    btn_choose_file = driver.find_element_by_css_selector("#file")

    btn_choose_file.send_keys(file_path)

    # Click submit button

    btn_submit = driver.find_element_by_css_selector("button[type='submit']")
    btn_submit.click()

finally:
    time.sleep(9)
    driver.quit()
