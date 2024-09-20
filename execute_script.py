import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math  # Добавил для вычислений, если нужно

driver = webdriver.Chrome()
driver.get("https://SunInJuly.github.io/execute_script.html")

# Получаем значение и производим вычисление
x = driver.find_element(By.ID, "input_value")
x_value = x.text
calculated_value = str(math.log(abs(12 * math.sin(int(x_value)))))

# Находим поле для ответа, скроллим к нему и вводим результат
answer = driver.find_element(By.ID, 'answer')
driver.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(calculated_value)

# Находим и кликаем по чекбоксу
cbx = driver.find_element(By.ID, "robotCheckbox")  # Прямо на чекбокс
cbx.click()

# Находим и кликаем по радиокнопке
rbtn = driver.find_element(By.ID, "robotsRule")  # Прямо на радиокнопку
rbtn.click()

# Находим и кликаем по кнопке Submit
submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit.click()
time.sleep(10)
