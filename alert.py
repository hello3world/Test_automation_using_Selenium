# Задание: принимаем alert
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/alert_accept.html")

# Находим и кликаем по кнопке Submit
submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit.click()

confirm = driver.switch_to.alert
confirm.accept()

num = driver.find_element(By.ID, "input_value")
num_text = num.text
text = driver.find_element(By.NAME, "text")
calculated_value = str(math.log(abs(12 * math.sin(int(num_text)))))
text.send_keys(calculated_value)

# Находим и кликаем по кнопке Submit
submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit.click()


time.sleep(10)
