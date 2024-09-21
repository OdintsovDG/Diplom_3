from selenium.webdriver.common.by import By


class ProfilePageLocators:

    # Кнопка "Выход"
    LOGOUT_BUTTON = By.XPATH, '//*[text()="Выход"]'
    # Кнопка "История заказов"
    ORDERS_HISTORY_BUTTON = By.XPATH, '//*[text()="История заказов"]'
    # Текст в разделе «История заказов»
    ORDERS_HISTORY_TEXT = By.XPATH, '//*[text()="Выполнен"]'
