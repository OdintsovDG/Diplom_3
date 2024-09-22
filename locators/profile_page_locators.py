from selenium.webdriver.common.by import By


class ProfilePageLocators:

    # Кнопка "Выход"
    LOGOUT_BUTTON = By.XPATH, '//*[text()="Выход"]'
    # Кнопка "История заказов"
    ORDERS_HISTORY_BUTTON = By.XPATH, '//*[text()="История заказов"]'
    # Текст в разделе «История заказов»
    ORDERS_HISTORY_TEXT = By.XPATH, '//*[text()="Выполнен"]'
    # Кнопка перехода в личный кабинет
    PERSONAL_AREA = By.XPATH, '//*[text()="Личный Кабинет"]'
    # Поле ввода "Email"
    EMAIL_FIELD = By.XPATH, '//input[@type = "text"]'
    # Поле ввода "Пароль"
    PASSWORD_FIELD = By.XPATH, '//input[@type = "password"]'
    # Кнопка "Войти" в форме ЛК
    LOGIN_BUTTON_IN_PA = By.XPATH, '//button[text() = "Войти"]'
