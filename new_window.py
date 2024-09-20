import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Функция для вычисления математического выражения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Открываем браузер и загружаем страницу
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")

# Явное ожидание появления кнопки
try:
    submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )

    # Прокручиваем страницу к кнопке с помощью JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)

    # Кликаем по кнопке
    submit.click()

    # Переключаемся на новую вкладку
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    # Явное ожидание появления значения для вычислений
    num = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    num_text = num.text
    calculated_value = calc(num_text)

    # Вводим вычисленное значение в поле ответа
    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(calculated_value)

    # Прокручиваем страницу к кнопке Submit, если она скрыта
    submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)

    # Кликаем по кнопке Submit
    submit.click()

    # Ждем некоторое время для проверки результата
    time.sleep(10)

finally:
    # Закрываем браузер
    driver.quit()
