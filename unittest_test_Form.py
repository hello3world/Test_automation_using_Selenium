import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestForm(unittest.TestCase):

    def test_form_1(self):
        driver = webdriver.Chrome()
        driver.get("http://suninjuly.github.io/registration1.html")

        # Заполняем обязательные поля
        first_name = driver.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        first_name.send_keys("Yauheni")

        last_name = driver.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        last_name.send_keys("Paulovich")

        email = driver.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email.send_keys("email@gmail.com")

        phone = driver.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        phone.send_keys("+377771156846")

        address = driver.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        address.send_keys("Yauheni")

        # Находим и кликаем по кнопке Submit
        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        # Подождем загрузки страницы
        time.sleep(2)

        # Проверяем, что мы на странице с текстом о том, что регистрация успешна
        welcome_text = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # Закрываем браузер
        driver.quit()

    def test_form_2(self):
        driver = webdriver.Chrome()
        driver.get("http://suninjuly.github.io/registration2.html")

        # Заполняем обязательные поля
        first_name = driver.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        first_name.send_keys("Yauheni")

        email = driver.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email.send_keys("email@gmail.com")

        phone = driver.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        phone.send_keys("+377771156846")

        address = driver.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        address.send_keys("Yauheni")

        # Находим и кликаем по кнопке Submit
        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        # Подождем загрузки страницы
        time.sleep(2)

        # Проверяем, что мы на странице с текстом о том, что регистрация успешна
        welcome_text = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    unittest.main()
