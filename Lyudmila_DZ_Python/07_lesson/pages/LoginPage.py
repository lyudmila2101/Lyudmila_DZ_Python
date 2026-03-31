import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:    
    def __init__(self, driver):
        self.driver = driver    
        self.wait = WebDriverWait(driver, 10)
        self.driver.maximize_window()

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def swag_labs(driver, username):
        username = driver.find_element(By.CSS_SELECTOR, '#username')
        username.send_keys("standard_user", Keys.RETURN)
        password = driver.find_element(By.CSS_SELECTOR, '#password')
        password.send_keys("secret_sauce", Keys.RETURN)
        button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        button.click() 
             
    
    
