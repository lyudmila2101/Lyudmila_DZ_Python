import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """
    Класс для работы с калькулятором на странице.
    Содержит методы для взаимодействия с элементами калькулятора.
    """
    
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.
        
        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        
        """
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(url)
        allure.attach(url, "URL страницы", allure.attachment_type.TEXT)
    
    @allure.step("Установка задержки: {delay} секунд")
    def delay_input_field(self, delay=5):
        """
        Устанавливает значение в поле задержки.
        
        Args:
            delay (int): Значение задержки в секундах. По умолчанию 5.
        """
        delay_locator = (By.ID, "delay")
        delay_input = self.wait.until(
            EC.presence_of_element_located(delay_locator)
        )
        delay_input.clear()
        delay_input.send_keys(str(delay))
        allure.attach(str(delay), "Установленная задержка", allure.attachment_type.TEXT)
    
    @allure.step("Нажатие кнопок:")
    def press_buttons(self):
        """
        Нажимает указанные кнопки калькулятора.
            
        """
    
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()    
    
    
    @allure.step("Получение результата вычисления")
    def result(self):
        self.wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="screen"]'), '15')
        )

        return self.driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text
            
    @allure.step("Очистка поля ввода")
    def clear_input(self):
        """
        Очищает поле ввода калькулятора.
        """
        input_locator = (By.ID, "input")
        input_field = self.wait.until(
            EC.presence_of_element_located(input_locator)
        )
        input_field.clear()
        allure.attach("Поле ввода очищено", "Действие", allure.attachment_type.TEXT)
    
    @allure.step("Ввод выражения: {expression}")
    def enter_expression(self, expression):
        """
        Вводит математическое выражение в поле ввода.
        
        Args:
            expression (str): Математическое выражение
        """
        input_locator = (By.ID, "input")
        input_field = self.wait.until(
            EC.presence_of_element_located(input_locator)
        )
        input_field.clear()
        input_field.send_keys(expression)
        allure.attach(expression, "Введенное выражение", allure.attachment_type.TEXT)
    
    @allure.step("Выбор операции: {operation}")
    def select_operation(self, operation):
        """
        Выбирает операцию из выпадающего списка.
        
        Args:
            operation (str): Операция (add, subtract, multiply, divide)
        """
        operation_locator = (By.ID, "selectOperation")
        operation_select = self.wait.until(
            EC.presence_of_element_located(operation_locator)
        )
        operation_select.click()
        
        operation_option = (By.XPATH, f"//option[@value='{operation}']")
        option = self.wait.until(
            EC.element_to_be_clickable(operation_option)
        )
        option.click()
        allure.attach(operation, "Выбранная операция", allure.attachment_type.TEXT)
    
    @allure.step("Включение/выключение защиты от дурака: {enabled}")
    def set_protection_mode(self, enabled=True):
        """
        Включает или выключает режим защиты от дурака.
        
        Args:
            enabled (bool): True - включить, False - выключить
        """
        checkbox_locator = (By.ID, "protect")
        checkbox = self.wait.until(
            EC.presence_of_element_located(checkbox_locator)
        )
        if checkbox.is_selected() != enabled:
            checkbox.click()
        
        status = "включен" if enabled else "выключен"
        allure.attach(f"Режим защиты {status}", "Действие", allure.attachment_type.TEXT)
  