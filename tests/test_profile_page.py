import allure
from data import TextOfElements


class TestProfilePage:

    @allure.title('Проверяем переход по клику на кнопку "История заказов"')
    def test_switch_orders_history_list(self, profile_page):
        profile_page.log_in()
        profile_page.click_on_orders_history_button()
        result = profile_page.find_order_history_element()
        assert result == TextOfElements.IS_DONE_TEXT

    @allure.title('Проверяем выход из аккаунта')
    def test_exit_account(self, profile_page):
        profile_page.log_in()
        profile_page.click_on_exit_from_account_button()
        result = profile_page.find_enter_button()
        assert result == TextOfElements.ENTER_TEXT
