import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@allure.suite("Калькулятор")
@allure.feature("Базовые операции")
class TestCalculator:
    """
    Тестовый класс для проверки функциональности калькулятора.
    """
    
    @pytest.fixture
    def driver(self):
        """
        Фикстура для инициализации и завершения работы WebDriver.
        
        Returns:
            WebDriver: Инициализированный экземпляр драйвера
        """
        with allure.step("Запуск Chrome драйвера"):
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            allure.attach("Chrome драйвер запущен", "Статус", allure.attachment_type.TEXT)
        
        yield driver
        
        with allure.step("Закрытие Chrome драйвера"):
            driver.quit()
            allure.attach("Chrome драйвер закрыт", "Статус", allure.attachment_type.TEXT)
    
    @allure.title("Проверка базовой операции сложения")
    @allure.story("Сложение")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Тест проверяет корректность выполнения операции сложения 7 + 8 = 15")
    @allure.tag("smoke", "positive")
    def test_calculator_addition(self, driver):
        """
        Тест проверки сложения двух чисел.
        
        Шаги:
        1. Открыть страницу калькулятора
        2. Установить задержку
        3. Нажать кнопки 7, +, 8, =
        4. Проверить результат
        """
        with allure.step("Инициализация страницы калькулятора"):
            calculator_page = CalculatorPage(driver)
        with allure.step("Инициализация страницы калькулятора"):
            
            calculator_page.open()
        with allure.step("Заполнение поле ввода delay"):    
            calculator_page.delay_input_field(delay=5)
        with allure.step("Нажатие ткнопок 7+8 "):    
            calculator_page.press_buttons()
        with allure.step("Получение результата"):
            result = calculator_page.result()
        
        with allure.step("Проверка результата"):
            allure.attach(result, "Полученный результат", allure.attachment_type.TEXT)
            assert result == "15", f"Ожидался результат 15, получен {result}"
    
    
