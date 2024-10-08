from data import Url
from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage
import allure


class SwitchPage(BasePage):
    @allure.step('Нажимаем кнопку Личный кабинет')
    def click_on_enter_account_button(self):
        self.click_on_element(SwitchPageLocators.PERSONAL_AREA)

    @allure.step('На странице личного кабинета ищем кнопку "Войти"')
    def find_enter_button(self):
        self.find_element_with_wait(SwitchPageLocators.LOGIN_BUTTON_IN_PA)
        return self.get_text_from_element(SwitchPageLocators.LOGIN_BUTTON_IN_PA)

    @allure.step('Нажимаем кнопку "Лента заказов"')
    def click_on_orders_list_button(self):
        self.click_on_element(SwitchPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Находим заголовок "Лента заказов""')
    def find_text_title_orders_feed(self):
        self.find_element_with_wait(SwitchPageLocators.ORDER_FEED)
        return self.get_text_from_element(SwitchPageLocators.ORDER_FEED)

    @allure.step('Нажимаем кнопку "Конструктор"')
    def click_on_constructor_button(self):
        self.get_url(Url.LOGIN_URL)
        self.click_on_element(SwitchPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Находим текст "Соберите бургер"')
    def find_text_make_burger(self):
        self.find_element_with_wait(SwitchPageLocators.MAKE_BURGER)
        return self.get_text_from_element(SwitchPageLocators.MAKE_BURGER)
