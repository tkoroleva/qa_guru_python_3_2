from selene.support.shared import browser
from selene import have


def test_search_passed(open_browser):
    browser.element('[name="q"]').type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_search_failed(open_browser):
    browser.element('[name="q"]').type('dfdgthtyhfgvfggb').press_enter()
    browser.element('[id="topstuff"]').should(have.text('ничего не найдено'))
