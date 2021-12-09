from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

#!!! DATA !!!#
user = input("Nhập tài khoản: ")
password = input("Nhập mật khẩu: ")
round_quiz = int(input("Chọn vòng: "))
round_1 = ["a","a","a","d","a","d","b","a","d","d","a","c","b","d","d","b","a","c","b","a"]
round_2 = ["c", "b", "d", "b", "a", "c", "d", "b", "c", "b", "b", "d", "d", "d", "a", "c", "b", "d", "c", "d"]
round_3 = ["c", "d", "b", "d", "b", "d", "d", "d", "b", "c", "d", "d", "d", "d", "a", "b", "a", "c", "d", "d"]
type_quiz = round_1
if round_quiz == 1:
    type_quiz = round_1
if round_quiz == 2:
    type_quiz = round_2
if round_quiz == 3:
    type_quiz = round_3


#!!! SETTINGS !!!#
ser = Service("chromedriver.exe")
settings_pref = {"profile.default_content_setting_values.notifications" : 2}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs",settings_pref)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

#!!! OPEN WEB !!!#
driver = webdriver.Chrome(service=ser, options=chrome_options)
wait = WebDriverWait(driver, 5)
driver.get("http://thi.giaothonghanoi.vn")

#lOGIN#
wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/a[1]'))).click()
driver.switch_to.frame(wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[9]/iframe'))))
wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[1]/p/input'))).send_keys(user)
wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/p/input'))).send_keys(password)
wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[4]/a'))).click()

#!!! OPEN EXAM PAGE !!!#
wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/ul/li[4]/a'))).click()
wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/ul/li[4]/ul/li[1]/a'))).click()
time.sleep(1)
wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/a'))).click()

#!!! CORRECT ANSWER !!!#
quest_number = 1
quest_count = 0
count = 1

try:
    for answer in type_quiz:
        wait.until(ec.element_to_be_clickable((By.ID, f"qt_2_{answer}_{quest_count}"))).click() 
        wait.until(ec.element_to_be_clickable((By.ID, f"a_qt_2_{quest_count}"))).click()
        quest_number += 1
        quest_count += 1
        count += 1
        if count == 8: # next list quest
            wait.until(ec.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/a[2]'))).click() 
            count = 1
        wait.until(ec.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/ul/li[{quest_number}]/a'))).click() 
except:
    driver.close()
    print("Complete quest !")