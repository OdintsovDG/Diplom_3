from selenium.webdriver.common.by import By


class LoginPageLocators:

    # Поле ввода "Email"
    EMAIL_FIELD = By.XPATH, '//input[@type = "text"]'
    # Поле ввода "Пароль"
    PASSWORD_FIELD = By.XPATH, '//input[@type = "password"]'
    # Кнопка "Войти" в форме ЛК
    LOGIN_BUTTON_IN_PA = By.XPATH, '//button[text() = "Войти"]'
