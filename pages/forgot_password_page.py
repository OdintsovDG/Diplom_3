from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
import helpers
import allure


class ForgotPasswordPage(BasePage):

    @allure.step('Кликаем по ссылке "Восстановить пароль"')
    def click_on_password_recovery_xref(self):
        self.click_on_element(ForgotPasswordPageLocators.RECOVERY_PASSWORD_XREF)

    @allure.step('Находим кнопку "Восстановить"')
    def find_recovery_button(self):
        self.find_element_with_wait(ForgotPasswordPageLocators.RECOVERY_BUTTON)
        return self.get_text_from_element(ForgotPasswordPageLocators.RECOVERY_BUTTON)

    @allure.step('Вводим Email')
    def set_email(self):
        email = helpers.gen_email()
        self.set_text_to_element(ForgotPasswordPageLocators.INPUT_EMAIL, email)

    @allure.step('Нажимаем кнопку "Восстановить"')
    def click_on_recover_button(self):
        self.click_on_element(ForgotPasswordPageLocators.RECOVERY_BUTTON)

    @allure.step('Находим поле ввода нового пароля, на странице восстановления пароля')
    def find_password_placeholder_text(self):
        self.find_element_with_wait(ForgotPasswordPageLocators.PLACEHOLDER_PASSWORD_FIELD)
        return self.get_text_from_element(ForgotPasswordPageLocators.PLACEHOLDER_PASSWORD_FIELD)

    @allure.step('Переходим на страницу введения нового пароля')
    def go_to_reset_password(self):
        self.click_on_password_recovery_xref()
        self.set_email()
        self.click_on_recover_button()

    @allure.step('Нажимаем кнопку "Показать/скрыть пароль"')
    def click_on_action_button_icon(self):
        self.click_on_element(ForgotPasswordPageLocators.ACTION_BUTTON_ICON)

    @allure.step('Кнопка "Показать/скрыть пароль" активна')
    def action_button_icon_on(self):
        self.find_element_with_wait(ForgotPasswordPageLocators.ACTION_BUTTON_ICON_ON)
        return self.get_text_from_element(ForgotPasswordPageLocators.ACTION_BUTTON_ICON_ON)
