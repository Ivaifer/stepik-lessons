import math
import time

from selenium import webdriver


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    x = browser.find_element(by='id', value='input_value').text
    answer = calc(x)
    field_for_input_answer = browser.find_element(by='id', value='answer')
    field_for_input_answer.send_keys(answer)
    button = browser.find_element(by='tag name', value='button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(by='id', value='robotCheckbox').click()
    browser.find_element(by='id', value='robotsRule').click()
    button.click()


finally:
    time.sleep(10)
    browser.quit()

