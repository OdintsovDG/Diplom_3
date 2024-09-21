from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from data import Timer


class BasePage:

    @allure.step('Подгружаем драйвер в конструктор')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загружаем страницу')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Ищем элемент на странице с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, Timer.TIMEOUT).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем появление элемента на странице (долго)')
    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, Timer.TIMEOUT_2).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Ищем элемент на странице с ожиданием возможности нажатия')
    def find_element_with_wait_to_click(self, locator):
        WebDriverWait(self.driver, Timer.TIMEOUT).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на элемент с ожиданием')
    def click_on_element_with_wait(self, locator):
        element = self.find_element_with_wait_to_click(locator)
        element.click()

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Вводим текст в элемент')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('Получаем текст элементов')
    def get_text_from_elements(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop(self, element_from, element_to):
        action = ActionChains(self.driver)
        from_element = self.find_element_with_wait(element_from)
        to_element = self.find_element_with_wait(element_to)
        action.drag_and_drop(from_element, to_element).perform()
