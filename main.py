from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import os
import wget
import time
from getpass import getpass

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")
print(driver.title)

username = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

login_name = input("Enter username: ")
passwrd = getpass("Enter password: ")
username.send_keys(login_name)
password.send_keys(passwrd)
submit = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

for _ in range(2):
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

searchbox = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
keyword = "#benz"
searchbox.send_keys(keyword)
time.sleep(2)

my_link = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()

n_scrolls = 2
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

n_anchors = driver.find_elements_by_tag_name('a')
anchors = [anchor.get_attribute('href') for anchor in n_anchors]

anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

print('Found ' + str(len(anchors)) + ' links to images')

images = []

for a in anchors:
    driver.get(a)
    time.sleep(5)
    img = driver.find_elements_by_tag_name('img')
    img = [i.get_attribute('src') for i in img]
    images.append(img[1])

path = os.getcwd()
path = os.path.join(path, keyword[1:] + 's')
os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

