from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Url, LogData
import allure


class ProfilePage(BasePage):

    @allure.step('Нажимаем кнопку "Личный кабинет"')
    def click_on_enter_account_button(self):
        self.click_on_element(MainPageLocators.PERSONAL_AREA)

    @allure.step('На странице личного кабинета ищем кнопку "Войти"')
    def find_enter_button(self):
        self.find_element_with_wait(LoginPageLocators.LOGIN_BUTTON_IN_PA)
        return self.get_text_from_element(LoginPageLocators.LOGIN_BUTTON_IN_PA)

    @allure.step('Входим в личный кабинет по логину и паролю')
    def log_in(self):
        self.get_url(Url.LOGIN_URL)
        self.set_text_to_element(LoginPageLocators.EMAIL_FIELD, LogData.EMAIL)
        self.set_text_to_element(LoginPageLocators.PASSWORD_FIELD, LogData.PASSWORD)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON_IN_PA)
        self.click_on_enter_account_button()

    @allure.step('Нажимаем кнопку «История заказов»')
    def click_on_orders_history_button(self):
        self.click_on_element(ProfilePageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Находим заказ с текстом "Выполнен" в разделе "История заказов"')
    def find_order_history_element(self):
        self.find_element_with_wait(ProfilePageLocators.ORDERS_HISTORY_TEXT)
        return self.get_text_from_element(ProfilePageLocators.ORDERS_HISTORY_TEXT)

    @allure.step('Выходим из аккаунта»')
    def click_on_exit_from_account_button(self):
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)
