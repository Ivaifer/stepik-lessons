import time

from selenium import webdriver

link = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()
selector = 'css selector'

try:
    browser.get(link)
    input_1 = browser.find_element(by=selector,
                                   value='div.first_block input.form-control.first')
    input_1.send_keys('Ivan')
    input_2 = browser.find_element(by=selector,
                                   value='div.first_block input.form-control.second')
    input_2.send_keys('Ivanov')
    input_3 = browser.find_element(by=selector,
                                   value='div.first_block input.form-control.third')
    input_3.send_keys('ivan@mail.ru')
    button = browser.find_element(by=selector, value='button')
    button.click()

    welcome_text_elt = browser.find_element(by='tag name', value='h1')

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
