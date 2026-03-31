from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

un = "input[name='username']"
push_login = driver.find_element(By.CSS_SELECTOR, un)
push_login.send_keys("tomsmith")

pw = "input[id='password']"
push_pass = driver.find_element(By.CSS_SELECTOR, pw)
push_pass.send_keys("SuperSecretPassword!")

sleep(3)

push_log = "button.radius"
push_log = driver.find_element(By.CSS_SELECTOR, push_log)
push_log.click()

success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(success_message.text)

sleep(5)

driver.quit()
