from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
import allure


class FeedPage(BasePage):

    @allure.step('Получаем номер заказа')
    def receive_orders_number_from_order_list(self):
        return self.get_text_from_element(FeedPageLocators.FIRST_ORDER_NUMBER_IN_LIST)

    @allure.step('Нажимаем на первый заказ в списке')
    def click_on_first_order(self):
        self.click_on_element(FeedPageLocators.FIRST_ORDER)

    @allure.step('Находим заголовок "Состав" в деталях заказа')
    def receive_text_from_order_details_popup(self):
        return self.get_text_from_element(FeedPageLocators.ELEMENT_FROM_ORDER_DETAILS)

    @allure.step('Получаем номер заказа из Истории заказов')
    def receive_orders_number_history(self):
        return self.get_text_from_element(FeedPageLocators.FIRST_ORDER_HISTORY)

    @allure.step('Получаем номер заказа из раздела "В работе"')
    def receive_orders_number_in_work_list(self):
        return self.get_text_from_element(FeedPageLocators.ORDER_IN_WORK_NUMBER)

    @allure.step('Получаем количество выполненых заказов за все время:')
    def receive_number_orders_done_alltime(self):
        return self.get_text_from_element(FeedPageLocators.ORDERS_DONE_ALLTIME)

    @allure.step('Получаем количество выполненых заказов за сегодня:')
    def receive_number_orders_done_today(self):
        return self.get_text_from_element(FeedPageLocators.ORDERS_DONE_TODAY)
