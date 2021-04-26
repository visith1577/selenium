from getpass import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.twitter.com/login")
print(driver.title)

username_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'

username = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, username_xpath)))
user = input('Enter instagram username: ')
username.send_keys(user)

my_password = getpass('Enter password: ')
password = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, password_xpath)))
password.send_keys(my_password)
password.send_keys(Keys.RETURN)
driver.maximize_window()
time.sleep(2)

search_box_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[' \
                   '1]/div/div/div/form/div[1]/div/div/div[2]/input '

search_input = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, search_box_xpath)))
time.sleep(2)
search_input.clear()
twitter_tag = input('Enter Hash_tag: ')

search_input.send_keys(twitter_tag)
search_input.send_keys(Keys.RETURN)



