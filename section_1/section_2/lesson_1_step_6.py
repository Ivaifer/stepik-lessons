import math
import time

from selenium import webdriver


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    chest = browser.find_element(by='id', value='treasure')
    x = chest.get_attribute('valuex')
    answer = calc(x)
    field_for_input_answer = browser.find_element(by='id', value='answer')
    field_for_input_answer.send_keys(answer)
    browser.find_element(by='id', value='robotCheckbox').click()
    browser.find_element(by='id', value='robotsRule').click()
    button = browser.find_element(by='css selector', value='button')
    button.click()


finally:
    time.sleep(10)
    browser.quit()

