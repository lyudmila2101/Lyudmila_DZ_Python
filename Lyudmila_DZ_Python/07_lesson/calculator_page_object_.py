import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  
    driver.maximize_window()    
    yield driver
    driver.quit()

def test_calculator(driver):    
    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.delay_input_field()
    calculator_page.press_buttons()
    calculator_page.result()
