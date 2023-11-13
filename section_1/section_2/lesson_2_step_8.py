import os, time

from selenium import webdriver

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

link = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element(by='name', value='firstname').send_keys('ivan')
    browser.find_element(by='name', value='lastname').send_keys('ivanpv')
    browser.find_element(by='name', value='email').send_keys('iva@mail.com')
    browser.find_element(by='name', value='file').send_keys(file_path)
    browser.find_element(by='tag name', value='button').click()
finally:
    time.sleep(7)
    browser.quit()
