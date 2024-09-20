from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/cats.html")

# Находим и кликаем по кнопке Submit
submit = driver.find_element(By.ID, "button")
submit.click()