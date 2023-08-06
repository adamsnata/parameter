import pytest
from selenium import webdriver
from selene import browser

BASE_URL = 'https://github.com/'


@pytest.fixture(params=[
    (1920, 1080), (1680, 1050), (2560, 1440)
])
def browser_desktop(request):
    browser.config.driver_options = webdriver.ChromeOptions()

    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]

    yield browser

    browser.quit()


@pytest.fixture(params=[
    (240, 320), (320, 240), (320, 480)
])
def browser_mobile(request):
    browser.config.driver_options = webdriver.ChromeOptions()

    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]

    yield browser

    browser.quit()


def test_github_desktop(browser_desktop):
    browser.open(BASE_URL)

    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()


def test_github_mobile(browser_mobile):
    browser.open(BASE_URL)

    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()
