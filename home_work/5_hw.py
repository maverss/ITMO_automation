'''
Создайте файл 5_hw.py в нем выполняйте все задания
1. Создайте функцию которая
a. переходит на страницу https://www.saucedemo.com/
b. находит элементы:
i. текстовое поле username
ii. текстовое поле password
iii. кнопку submit
c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”
'''

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.CSS_SELECTOR, "#user-name")

if username is None:
    print('Element not found')
else:
    print('Element found')
    
password = driver.find_element(By.CSS_SELECTOR, "#password")

if username is None:
    print('Element not found')
else:
    print('Element found')

submit = driver.find_element(By.XPATH, "//div/form/input")

if username is None:
    print('Element not found')
else:
    print('Element found')