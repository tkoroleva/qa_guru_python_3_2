import pytest
from selene.support.shared import browser
from selene import be


@pytest.fixture()
def set_browser_size():
    browser.config.window_height = 900
    browser.config.window_width = 1600


@pytest.fixture()
def open_browser(set_browser_size):
    browser.open('https://google.com')


@pytest.fixture()
def check_blank_search(open_browser):
    browser.element('[name="q"]').should(be.blank)
