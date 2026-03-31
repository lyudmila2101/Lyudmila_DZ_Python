# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# 
# from pages.MainPage import MainPage
# from pages.ResultPage import ResultPage
# 
# def test_calculator():
    # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# 
# 
# 
# test_calculator(browser):
# driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
# 
# page.set_delay(45)
# 
# page.press_button('7')
# page.press_button('+')
# page.press_button('8')
# page.press_button('=')
# 
# wait = WebDriverWait(browser, 10)  
# 
# result = page.get_result()
# assert result == "15"
# 
# def browser():
    # browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().inst
    # 
# def test_calculator():
    # browser.get = ("https://bonigarcia.dev/selenium-webdriver-java/slow-calcula
# 
# 
    # wait = WebDriverWait(browser, 10)    
    # delay = browser.find_element(By.CSS_SELECTOR, "#delay")
    # delay.clear()
    # delay.send_keys("45")
    # button_1 = browser.find_element(By.XPATH, "//span[text()='7']").click()
    # button_2 = browser.find_element(By.XPATH, "//span[text()='+']").click()
    # button_3 = browser.find_element(By.XPATH, "//span[text()='8']").click()
    # button_4 = browser.find_element(By.XPATH, "//span[text()='=']").click()
# 
# 
    # result = WebDriverWait(browser, 50).until(
    # EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"),"15")
# )
    # assert result