from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

wait = WebDriverWait(driver, 10)
blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
blue_button.click()

sleep(3)

driver.quit()


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

wait = WebDriverWait(driver, 10)
blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
blue_button.click()

sleep(3)

driver.quit()


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

wait = WebDriverWait(driver, 10)
blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
blue_button.click()

sleep(3)

driver.quit()










