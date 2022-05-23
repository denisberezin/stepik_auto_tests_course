"""
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.
"""


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
import os


site = "http://suninjuly.github.io/file_input.html"




try:
    browser = webdriver.Chrome()
    browser.get(site)

    firstname_input = browser.find_element_by_css_selector("[name='firstname']")
    firstname_input.send_keys("Ivan")

    lastname_input = browser.find_element_by_css_selector("[name='lastname']")
    lastname_input.send_keys("Ivanov")

    email_input = browser.find_element_by_css_selector("[name='email']")
    email_input.send_keys("ivan.ivanov@yandex.ru")


    element = browser.find_element_by_css_selector("[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
