# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")

name = driver.find_element(By.NAME, "firstname")
name.send_keys("Yauheni")

last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys("Paulovich")

email = driver.find_element(By.NAME, "email")
email.send_keys("e.pavlovich29@gmail.com")

btn_file_load = driver.find_element(By.XPATH, '//input[@type="file"]')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
btn_file_load.send_keys(file_path)

# Находим и кликаем по кнопке Submit
submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit.click()
time.sleep(10)
