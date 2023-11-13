import math
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button = browser.find_element(by='id', value='book')
    button.click()
    x = browser.find_element(by='id', value='input_value').text
    answer = calc(x)
    field_for_input_answer = browser.find_element(by='id', value='answer')
    field_for_input_answer.send_keys(answer)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button = browser.find_element(by='id', value='solve')
    button.click()


finally:
    time.sleep(30)
    browser.quit()

