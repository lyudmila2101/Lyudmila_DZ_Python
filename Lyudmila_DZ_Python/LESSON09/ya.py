from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


#browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) #так называется драйвер-менеджер для Firefox

def make_screenshoot(browser):
    browser.maximize_window()   #для разворачивания окна
    browser.get("https://ya.ru/") #для перехода на нужную страницу
    sleep(5) #для паузы на загрузку контента страницы

    browser.save_screenshot("./ya_"+browser.name+".png") #для сохранения скриншота
    browser.quit() #для закрытия окна 


chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

make_screenshoot(chrome)
make_screenshoot(ff)