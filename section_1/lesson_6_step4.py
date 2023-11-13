import time

from selenium import webdriver

link = 'http://suninjuly.github.io/find_xpath_form'

browser = webdriver.Chrome()

try:

    browser.get(link)

    input1 = browser.find_element(by='tag name', value='input')
    input1.send_keys('Ivan')
    input2 = browser.find_element(by='name', value='last_name')
    input2.send_keys('Ivanov')
    input3 = browser.find_element(by='class name', value='form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id', value='country')
    input4.send_keys("Russia")
    button = browser.find_element(by='xpath',
                                  value='//div/button[contains(text(), "Submit")]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
