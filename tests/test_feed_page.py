import allure
from data import TextOfElements
import logging
logging.basicConfig(level=logging.INFO)


class TestOrderListPage:

    @allure.title('Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями заказа')
    def test_click_on_order_open_order_details(self, feed_page):
        feed_page.click_on_first_order()
        result = feed_page.receive_text_from_order_details_popup()
        assert result == TextOfElements.ELEMENT_FROM_ORDER_DETAILS_TEXT

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» '
                  'отображаются на странице «Лента заказов»,')
    def test_order_number_in_order_history(self, feed_page, profile_page, main_page, switch_page):
        profile_page.log_in()
        switch_page.click_on_constructor_button()
        main_page.make_order()
        main_page.overlay_disappearance()
        main_page.close_window_with_details()
        switch_page.click_on_enter_account_button()
        profile_page.click_on_orders_history_button()
        order_number_history = feed_page.receive_orders_number_history()
        switch_page.click_on_orders_list_button()
        order_number_order_list = feed_page.receive_orders_number_from_order_list()
        assert order_number_order_list == order_number_history
        logging.info(f'номер заказа в Листе заказа: {order_number_order_list},\n'
                     f'номер заказа в Истории заказа: {order_number_history}')

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_order_number_in_work(self, feed_page, profile_page, main_page, switch_page):
        profile_page.log_in()
        switch_page.click_on_constructor_button()
        main_page.make_order()
        main_page.close_window_with_details()
        switch_page.click_on_orders_list_button()
        order_number_order_list = feed_page.receive_orders_number_from_order_list()
        order_number_history = feed_page.receive_orders_number_history()
        order_number_in_work = feed_page.receive_orders_number_in_work_list()
        assert order_number_in_work in order_number_order_list
        logging.info(f'номер заказа в Листе заказа: {order_number_order_list},\n'
                     f'номер заказа в Истории заказа: {order_number_history}, в работе: {order_number_in_work}')

    @allure.title('Проверяем, что при создании нового заказа счётчик "Выполнено за все время" увеличивается')
    def test_orders_done_alltime(self, feed_page, profile_page, main_page, switch_page):
        profile_page.log_in()
        switch_page.click_on_orders_list_button()
        before_order = feed_page.receive_number_orders_done_alltime()
        switch_page.click_on_constructor_button()
        main_page.make_order()
        main_page.close_window_with_details()
        switch_page.click_on_orders_list_button()
        after_order = feed_page.receive_number_orders_done_alltime()
        assert int(after_order) == int(before_order) + 1
        logging.info(f'количество заказов ДО создания нового: {before_order},\n'
                     f'количество заказов ПОСЛЕ создания нового: {after_order}')

    @allure.title('Проверяем, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_orders_done_today(self, feed_page, profile_page, main_page, switch_page):
        profile_page.log_in()
        switch_page.click_on_orders_list_button()
        before_order = feed_page.receive_number_orders_done_today()
        switch_page.click_on_constructor_button()
        main_page.make_order()
        main_page.close_window_with_details()
        switch_page.click_on_orders_list_button()
        after_order = feed_page.receive_number_orders_done_today()
        assert int(after_order) == int(before_order) + 1
        logging.info(f'количество заказов ДО создания нового: {before_order},\n'
                     f'количество заказов ПОСЛЕ создания нового: {after_order}')
