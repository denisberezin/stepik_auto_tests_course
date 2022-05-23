from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



site = "http://suninjuly.github.io/math.html"




try:
    browser = webdriver.Chrome()
    browser.get(site)

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_css_selector("[id='answer']")
    input.send_keys(str(y))

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
