from selenium.webdriver.common.by import By


class SwitchPageLocators:

    # Кнопка перехода в личный кабинет
    PERSONAL_AREA = By.XPATH, '//*[text()="Личный Кабинет"]'
    # Кнопка "Войти" в форме ЛК
    LOGIN_BUTTON_IN_PA = By.XPATH, '//button[text() = "Войти"]'
    # Кнопка перехода в "Конструктор"
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text() = "Конструктор"]'
    # Заголовок в разделе "Конструктор"
    MAKE_BURGER = By.XPATH, './/*[text()="Соберите бургер"]'
    # Кнопка "Лента заказов"
    ORDER_FEED_BUTTON = By.XPATH, './/*[contains(@href, "feed")]'
    # Заголовок в разделе "Лента заказов"
    ORDER_FEED = By.XPATH, './/*[text()="Лента заказов"]'
