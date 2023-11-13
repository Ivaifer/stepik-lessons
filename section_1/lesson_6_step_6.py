from selenium import webdriver
import time

link = 'http://suninjuly.github.io/huge_form.html'

browser = webdriver.Chrome()

try:
    browser.get(link)
    elements = browser.find_elements(by='tag name', value='input')
    for element in elements:
        element.send_keys('some text')
    button = browser.find_element(by='tag name', value='button')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
    