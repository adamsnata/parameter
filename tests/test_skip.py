import pytest
from selenium import webdriver
from selene import browser

BASE_URL = 'https://github.com/'


@pytest.fixture(params=[(1920, 1080), (320, 240),
                        (2560, 1440), (240, 320)],
                ids=['desktop', 'mobile',
                     'desktop', 'mobile'])
def config_browser(request):
    # Obtaining the unique identifier of the current test case
    id = request.node.callspec.id

    browser.config.driver_options = webdriver.ChromeOptions()

    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]

    yield browser, id

    browser.quit()


def test_github_desktop(config_browser):
    browser, id = config_browser
    if 'mobile' in id:
        pytest.skip('The mobile aspect ratio is not suitable for the test.')

    browser.open(BASE_URL)

    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()


def test_github_mobile(config_browser):
    browser, id = config_browser
    if 'desktop' in id:
        pytest.skip('The desktop aspect ratio is not suitable for the test.')

    browser.open(BASE_URL)

    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()
