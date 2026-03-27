import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Authpage import Authpage
from Mainpage import Mainpage
from Cartpage import Cartpage
from Orderpage import Orderpage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window() 
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_swag_labs(driver):
    
    auth_page = Authpage(driver)
    auth_page.enter_login("standard_user")
    auth_page.enter_password("secret_sauce")
    auth_page.click_button()
    

    main_page = Mainpage(driver)    
    main_page.add_to_cart()
    main_page.go_to_cart()
    
    cart_page = Cartpage(driver)       
    cart_page.click_checkout()

    order_page = Orderpage(driver)
    order_page.fill_name('Lyudmila')
    order_page.fill_last_name('Kuznetsova')
    order_page.fill_code('428027')
    order_page.click_cont()
    total = order_page.get_summary()

    #assert total == "Total: $58.29"    