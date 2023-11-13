import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()

try:
    browser.get(link)
    number_1 = int(browser.find_element(by='id', value='num1').text)
    number_2 = int(browser.find_element(by='id', value='num2').text)
    select = Select(browser.find_element(by='tag name', value='select'))
    answer = number_1 + number_2
    select.select_by_value(str(answer))
    button = browser.find_element(by='css selector', value='button')
    button.click()
finally:
    time.sleep(8)
    browser.quit()

