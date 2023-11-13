import math
import time

from selenium import webdriver


link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    button = browser.find_element(by='tag name', value='button')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(by='id', value='input_value').text
    answer = calc(x)
    field_for_input_answer = browser.find_element(by='id', value='answer')
    field_for_input_answer.send_keys(answer)
    button = browser.find_element(by='tag name', value='button')
    button.click()


finally:
    time.sleep(10)
    browser.quit()

