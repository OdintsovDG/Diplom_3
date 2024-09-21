from selenium.webdriver.common.by import By


class FeedPageLocators:

    # Закрыть всплывающее окно "Детали заказа"
    CLOSE_POP_UP_BUTTON = By.XPATH, '//*[contains(@class, "Modal_modal__close")]'
    # Номер первого заказа в ленте заказов
    FIRST_ORDER_NUMBER_IN_LIST = By.XPATH, '(.//*[contains(@class, "text text_type_digits-default")])[1]'
    # Первый заказ в ленте заказов
    FIRST_ORDER = By.XPATH, '(.//*[contains(@class, "OrderHistory_link")])[1]'
    # Заголовок "Состав" окна "Детали заказа"
    ELEMENT_FROM_ORDER_DETAILS = By.XPATH, './/*[text()="Cостав"]'
    # Номер последнего заказа в "История заказов"
    FIRST_ORDER_HISTORY = By.XPATH, '(.//*[contains(@class, "text text_type_digits-default")])[1]'
    # Номер заказа в разделе "В работе"
    ORDER_IN_WORK_NUMBER = By.XPATH, '(//*[@class="text text_type_digits-default mb-2"])[1]'
    # Выполнено заказов за всё время
    ORDERS_DONE_ALLTIME = By.XPATH, '(.//*[contains(@class, "OrderFeed_number")])[1]'
    # Выполнено заказов за сегодня
    ORDERS_DONE_TODAY = By.XPATH, '(.//*[contains(@class, "OrderFeed_number")])[2]'
