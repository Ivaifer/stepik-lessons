
import time

from selenium import webdriver


link = 'http://suninjuly.github.io/cats.html'

browser = webdriver.Chrome()




try:
    browser.get(link)
    browser.find_element(by='id', value='button')


finally:
    time.sleep(1)
    browser.quit()

