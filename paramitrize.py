import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Функция для вычисления правильного ответа
def calculate_answer():
    return str(math.log(int(time.time())))


# Параметризация теста - передаем список URL для тестирования
@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])

def test_stepik(link):
    # Настраиваем Selenium WebDriver для Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        # Открываем нужную страницу
        driver.get(link)

        # Ждем появления кнопки для авторизации и кликаем на нее
        button_enter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text() = 'Войти']")))
        button_enter.click()

        # Вводим логин
        login_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "login"))
        )
        login_field.send_keys("e.pavlovich29@gmail.com")

        # Вводим пароль
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("*********")

        # Нажимаем кнопку для входа в систему
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Войти']")))
        submit_button.click()

        # Ждем, пока не исчезнет поп-ап с авторизацией
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element((By.ID, "ember517"))
            # Возможно, нужно будет уточнить локатор
        )

        # Вычисляем ответ
        answer = calculate_answer()

        # Находим поле для ответа, очищаем его и вводим ответ
        answer_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        answer_field.clear()
        answer_field.send_keys(answer)

        # Находим кнопку "Отправить" и кликаем по ней
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            "button.submit-submission")
        submit_button.click()

        # Ожидаем появления фидбека о правильности ответа
        feedback = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "smart-hints__hint"))
        )

        # Проверяем, что фидбек содержит "Correct!"
        assert feedback.text == "Correct!", f"Неверный текст фидбека: {feedback.text}"

    finally:
        # Закрываем браузер
        driver.quit()