from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопка перехода в "Конструктор"
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text() = "Конструктор"]'
    # Заголовок в разделе "Конструктор"
    MAKE_BURGER = By.XPATH, './/*[text()="Соберите бургер"]'
    # Кнопка "Лента заказов"
    ORDER_FEED_BUTTON = By.XPATH, './/*[contains(@href, "feed")]'
    # Заголовок в разделе "Лента заказов"
    ORDER_FEED = By.XPATH, './/*[text()="Лента заказов"]'
    # Булка "Краторная булка N-200i"
    KRATOR_BUN_N200I = By.XPATH, './/*[contains(@href, "61c0c5a71d1f82001bdaaa6c")]'
    # Заголовок окна "Детали ингредиента"
    DETAILS_POP_UP = By.XPATH, '//*[text()="Детали ингредиента"]'
    # Всплывающее окно "Детали ингредиента" открыто
    POP_UP_OPENED = By.XPATH, './*[contains(@class,"Modal_modal_opened")]'
    # Закрыть всплывающее окно "Детали ингредиента"
    CLOSE_POP_UP_BUTTON = By.XPATH, (
        '//*[contains(@class, "Modal_modal__contentBox")]/following::*[contains(@class, "Modal_modal__close")][1]')
    # Зона корзины/сбора заказа
    ORDER_BASKET = By.XPATH, '//*[contains(@class, "BurgerConstructor_basket__list__l9dp_")]'
    # Счетчик количества ингридиентов одного типа
    COUNTER = By.XPATH, '(.//*[contains(@class, "counter_counter__num__3nue1")])[2]'
    # Кнопка "Оформить заказ"
    ORDER_BUTTON = By.XPATH, '//button[text() = "Оформить заказ"]'
    # Всплывающее окно подтверждения, с номером заказа
    DETAILS_ORDER_IN_WORK = By.XPATH, './/*[text()="Ваш заказ начали готовить"]'
    # Закрыть всплывающее окно подтверждения, с номером заказа
    CLOSE_BUTTON_DETAILS = By.XPATH, (
        '//*[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//button')
