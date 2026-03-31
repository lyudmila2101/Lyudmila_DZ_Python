from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


driver.get( "https://www.labirint.ru/" )  # зайти на сайт лабиринт 


search_field =  "#search-field"           # Найти книги по слову Python
serch_input = driver.find_element(By.CSS_SELECTOR, search_field)
serch_input.send_keys("Python",Keys.RETURN)


sleep(3)

books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")
print(len(books)) 


# books = WebDriverWait(driver, 10).until(
#      EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card"))
# )
for book in books:
    title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
    price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text
try:
        author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
except: 
        author = "Автор не указан"       
    

print(f"{author} \t {title} \t {price}")    
    

sleep(10)


#print(title + "\t" + price + "\t")
# зайти на лабиринт
# найти книги по слову Python
# собрать все карточки товаров
# вывести в консоль инфо:название + автор + цена

# driver.find_elements_by_class_name("product-card")
#   print(driver.page_source)
# собрать все карточки товаров

        #вывести длину списка books

# вывести в консоль инфо:название + автор + цена
#from selenium.common.exceptions import NoSuchElementException

# try:
    #     author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
    # except: 
    #     author = "Автор не указан"          