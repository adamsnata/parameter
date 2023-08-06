import pytest
from selenium import webdriver
from selene import browser

BASE_URL = 'https://github.com/'


@pytest.fixture(params=[
    (1920, 1080), (320, 240),
    (2560, 1440), (240, 320)
])
def browser_config(request):
    browser.config.driver_options = webdriver.ChromeOptions()

    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]

    yield browser

    browser.quit()


desktop = pytest.mark.parametrize('browser_config', [(1920, 1080), (2560, 1440)], indirect=True)
mobile = pytest.mark.parametrize('browser_config', [(320, 240), (240, 320)], indirect=True)


@desktop
def test_github_desktop(browser_config):
    browser.open(BASE_URL)

    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()


@mobile
def test_github_mobile(browser_config):
    browser.open(BASE_URL)

    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()
