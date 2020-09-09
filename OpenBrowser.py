from selenium import webdriver
from getpass import getpass
import time


usr =input("Enter your UserID:")
pwd=getpass("Enter your password:")

driver=webdriver.Chrome("E:\\Python-poc\\Python-Poc\\chromedriver_win32\\chromedriver")
driver.get("http://localhost:8100/login")

time.sleep(5)
userId_box =driver.find_element_by_id('userId').click()
userId_box.send_keys(usr)

password_box =driver.find_element_by_id('passwordId').click()
password_box.send_keys(pwd)

login_button=driver.find_element_by_id("login").click()
