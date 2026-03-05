from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

wait = WebDriverWait(driver, 10)
button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
button.click()
driver.switch_to.alert.accept()

search_button = "button.btn-primary"
button_input = driver.find_element(By.CSS_SELECTOR, search_button)
button.click()
driver.switch_to.alert.accept()

sleep(2)


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

wait = WebDriverWait(driver, 10)
button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
button.click()
driver.switch_to.alert.accept()


search_button = "button.btn-primary"
button_input = driver.find_element(By.CSS_SELECTOR, search_button)
button.click()
driver.switch_to.alert.accept()

sleep(2)


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

wait = WebDriverWait(driver, 10)
button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
button.click()
driver.switch_to.alert.accept()


search_button = "button.btn-primary"
button_input = driver.find_element(By.CSS_SELECTOR, search_button)
button.click()
driver.switch_to.alert.accept()

sleep(2)

















