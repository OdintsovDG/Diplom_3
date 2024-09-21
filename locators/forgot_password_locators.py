from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    # Гиперссылка "Восстановить пароль"
    RECOVERY_PASSWORD_XREF = By.XPATH, '//*[text()="Восстановить пароль"]'
    # Кнопка "Восстановить"
    RECOVERY_BUTTON = By.XPATH, '//*[text()="Восстановить"]'
    # Поле ввода "Email"
    INPUT_EMAIL = By.XPATH, '//input[@name="name"]'
    # Плейсхолдер в поле ввода "Пароль"
    PLACEHOLDER_PASSWORD_FIELD = By.XPATH, '//*[text()="Пароль"]'
    # Кнопка "Показать/скрыть пароль"
    ACTION_BUTTON_ICON = By.XPATH, '//div[@class="input__icon input__icon-action"]'
    ACTION_BUTTON_ICON_ON = By.XPATH, '//*[contains(@class, "placeholder-focused") and text()="Пароль"]'
