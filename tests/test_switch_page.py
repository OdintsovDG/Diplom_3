import allure
from data import TextOfElements


class TestSwitchPage:

    @allure.title('Проверяем переход по клику на кнопку "Личный кабинет"')
    def test_switch_personal_account(self, switch_page):
        switch_page.click_on_enter_account_button()
        result = switch_page.find_enter_button()
        assert result == TextOfElements.ENTER_TEXT

    @allure.title('Проверяем переход по клику на кнопку "Лента заказов"')
    def test_switch_orders_list(self, switch_page):
        switch_page.click_on_orders_list_button()
        result = switch_page.find_text_title_orders_feed()
        assert result == TextOfElements.TITLE_ORDERS_TEXT

    @allure.title('Проверяем переход по клику на кнопку "Конструктор"')
    def test_switch_to_constructor(self, switch_page):
        switch_page.click_on_constructor_button()
        result = switch_page.find_text_make_burger()
        assert result == TextOfElements.MAKE_BURGER_TEXT
