# Задание: ждем нужный текст на странице
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
#
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
#
# Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

# Находим и кликаем по кнопке Submit
price = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

# Находим и кликаем по кнопке Submit
submit = driver.find_element(By.ID, 'book')
submit.click()

x = driver.find_element(By.ID, "input_value")
x_value = x.text
calculated_value = str(math.log(abs(12 * math.sin(int(x_value)))))

answer = driver.find_element(By.ID, 'answer')
driver.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(calculated_value)

submit = driver.find_element(By.ID, "solve")
submit.click()

time.sleep(10)