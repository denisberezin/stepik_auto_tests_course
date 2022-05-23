"""
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
Отправьте полученное число в качестве ответа на это задание.
"""


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

site = "http://suninjuly.github.io/redirect_accept.html"




try:
    browser = webdriver.Chrome()
    browser.get(site)

    button = browser.find_element_by_css_selector("button.trollface")
    button.click()

    confirm = browser.switch_to.window(browser.window_handles[1])
    
    value = browser.find_element_by_css_selector("[id='input_value']").text

    result_input = browser.find_element_by_css_selector("[id='answer']")
    result_input.send_keys(calc(value))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
