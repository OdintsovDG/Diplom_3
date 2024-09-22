from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    @allure.step('Кликаем по ингредиенту "Краторная булка N-200i"')
    def click_on_bun_ingredient(self):
        self.click_on_element(MainPageLocators.KRATOR_BUN_N200I)

    @allure.step('Находим текст "Детали ингредиента", во всплывающем окне')
    def find_details_text(self):
        self.find_element_with_wait(MainPageLocators.DETAILS_POP_UP)
        return self.get_text_from_element(MainPageLocators.DETAILS_POP_UP)

    @allure.step('Кликаем по крестику и закрываем всплывающее окно "Детали ингредиента"')
    def click_on_close_popup_button(self):
        self.click_on_element(MainPageLocators.CLOSE_POP_UP_BUTTON)

    @allure.step('На главной странице находим текст "Соберите бургер"')
    def find_text_make_burger_after_popup_close(self):
        self.find_element_with_wait(MainPageLocators.MAKE_BURGER)
        return self.get_text_from_element(MainPageLocators.MAKE_BURGER)

    @allure.step('Перетаскиваем элемент в корзину заказа')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop(MainPageLocators.KRATOR_BUN_N200I, MainPageLocators.ORDER_BASKET)

    @allure.step('Проверяем счетчик')
    def count_ingredients(self):
        return self.get_text_from_elements(MainPageLocators.COUNTER)

    @allure.step('Нажимаем кнопку "Оформить заказ"')
    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Собираем и оформляем заказ')
    def make_order(self):
        self.drag_and_drop_ingredient()
        self.click_on_order_button()

    @allure.step('Проверяем, что текст во всплывающем окне - "Ваш заказ начали готовить"')
    def receive_order_in_work_text(self):
        return self.get_text_from_element(MainPageLocators.DETAILS_ORDER_IN_WORK)

    @allure.step('Закрываем окно с деталями заказа')
    def close_window_with_details(self):
        self.wait_for_visibility(MainPageLocators.CLOSE_BUTTON_DETAILS)
        self.click_on_element_with_wait(MainPageLocators.CLOSE_BUTTON_DETAILS)

    @allure.step('Ожидаем исчезновения модального окна')
    def overlay_disappearance(self):
        self.wait_for_overlay_disappearance()
