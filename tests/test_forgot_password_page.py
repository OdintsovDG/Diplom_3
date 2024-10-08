import allure
from data import TextOfElements


class TestForgotPasswordPage:

    @allure.title('Проверяем переход на страницу восстановления пароля по ссылке «Восстановить пароль»')
    def test_switch_password_recovery(self, forgot_password_page):
        forgot_password_page.click_on_password_recovery_xref()
        result = forgot_password_page.find_recovery_button()
        assert result == TextOfElements.RECOVER_TEXT

    @allure.title('Проверяем возможность ввода почты и клика по кнопке «Восстановить»')
    def test_set_email_and_click_on_recovery_button(self, forgot_password_page):
        forgot_password_page.go_to_reset_password()
        result = forgot_password_page.find_password_placeholder_text()
        assert result == TextOfElements.PASSWORD_TEXT

    @allure.title('Проверяем, что клик по кнопке "Показать/скрыть пароль" делает поле активным — подсвечивает его')
    def test_click_on_button_show_hide_password(self, forgot_password_page):
        forgot_password_page.go_to_reset_password()
        forgot_password_page.click_on_action_button_icon()
        result = forgot_password_page.action_button_icon_on()
        assert result == TextOfElements.PASSWORD_TEXT
