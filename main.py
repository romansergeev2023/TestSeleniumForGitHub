# Задание: ждем нужный текст на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
browser.find_element(By.ID, "book").click()

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)
textField = browser.find_element(By.CSS_SELECTOR, 'input[id = "answer"]')
textField.send_keys(y)
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(10)
