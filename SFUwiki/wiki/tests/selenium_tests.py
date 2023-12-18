from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# #1 тест (Тест логина и перехода в личный кабинет)
# link = 'http://localhost:5173/'
# browser = webdriver.Chrome()
# browser.get(link)
# login_nav_button = browser.find_element(By.XPATH, '//*[@id="navbar-default"]/ul/li[6]/a')
# login_nav_button.click()
# time.sleep(2)
# login_input = browser.find_element(By.XPATH, '//*[@id="username"]')
# login_input.send_keys('qwerty')
# pass_input = browser.find_element(By.XPATH, '//*[@id="password"]')
# pass_input.send_keys('1234')
# login_button = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/form/button')
# login_button.click()
# time.sleep(3)
# username_link = browser.find_element(By.XPATH, '//*[@id="navbar-default"]/ul/li[6]/div/a')
# assert username_link is not None
# username_link.click()
# time.sleep(2)
# username_h1 = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div[1]/h1')
# assert username_h1.text == 'qwerty'
# time.sleep(5)
# print('Тест пройден успешно, пользователь может залогиниться и зайти в свой личный кабинет')

# # 2 тест (Путь пользователя через поиск преподавателя)
# link = 'http://localhost:5173/'
# browser = webdriver.Chrome()
# browser.get(link)
# time.sleep(2)
# button = browser.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/a[1]')
# button.click()
# time.sleep(2)
# search_teacher = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/input')
# search_teacher.send_keys('Брежнев Руслан Владимирович')
# time.sleep(2)
# teacher_link = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/a')
# teacher_link.click()
# time.sleep(3)
# teacher_name = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div/div/div[1]/div/h5').text
# assert teacher_name == 'Брежнев Руслан Владимирович'

#
# 3 тест (Путь пользователя через выбор Института, кафедры и преподавателя из списка по кафедре, проверка работы карусели)
link = 'http://localhost:5173/'
browser = webdriver.Chrome()
browser.get(link)
institutes_list_link = browser.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/a[2]')
institutes_list_link.click()
time.sleep(2)
choosen_institute_link = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/a/a')
choosen_institute_link.click()
time.sleep(2)
carousel_button_next = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/section/button[2]')
carousel_button_next.click()
time.sleep(1)
carousel_button_prev = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/section/button[1]')
carousel_button_prev.click()
time.sleep(1)
choosen_department_link = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div[2]/a[2]')
choosen_department_link.click()
time.sleep(2)
choosen_teacher_link = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/a[1]/div/div/div[2]/a')
choosen_teacher_link.click()
time.sleep(2)
choosen_teacher_name = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div/div/div[1]/div/h5').text
assert choosen_teacher_name == 'Дмитрий'