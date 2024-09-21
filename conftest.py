import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from data import Url
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from pages.switch_page import SwitchPage
from pages.feed_page import FeedPage
from pages.forgot_password_page import ForgotPasswordPage


@allure.step('Инициализируем драйвер')
@pytest.fixture
def driver():
    service = webdriver.chrome.service.Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    options.add_argument("--window_size=1920,1080")
    yield driver
    driver.quit()


@pytest.fixture
def profile_page(driver):
    page = ProfilePage(driver)
    page.get_url(Url.MAIN_PAGE_URL)
    return page


@pytest.fixture
def forgot_password_page(driver):
    page = ForgotPasswordPage(driver)
    page.get_url(Url.LOGIN_URL)
    return page


@pytest.fixture
def switch_page(driver):
    page = SwitchPage(driver)
    page.get_url(Url.MAIN_PAGE_URL)
    return page


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.get_url(Url.MAIN_PAGE_URL)
    return page


@pytest.fixture
def feed_page(driver):
    page = FeedPage(driver)
    page.get_url(Url.FEED_PAGE_URL)
    return page
