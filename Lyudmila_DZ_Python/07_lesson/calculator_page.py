import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
    def delay_input_field(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        element.clear()
        element.send_keys("45")


    def press_buttons(self):
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            xpath = f"//span[text()='{button}']"
            self.driver.find_element(By.XPATH, xpath).click()


    def result(self):
        result = WebDriverWait(self.driver, 70).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"),"15")   
    )       
  


















