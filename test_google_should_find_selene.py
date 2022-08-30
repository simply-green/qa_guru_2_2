from selene import Browser, Config
from selene.support.shared import browser,config
from selene import be, have
import pytest

@pytest.fixture()
def configure_small():
    #выбираем разрешение iPhone 12 Pro
    browser.config.window_height = 844
    browser.config.window_width = 390
    browser.open('https://google.com/ncr')

def test_searching(configure_small):
    #Сравнение результатов
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

@pytest.fixture()
def configure_negative():
    #Выбираем разрешение Samsung S8+
    browser.config.window_height = 740
    browser.config.window_width = 360
    browser.open('https://google.com/ncr')


def test_negative(configure_negative):
    #Проверяем негативный вариант
    browser.element('[name="q"]').should(be.blank).type('gomez').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))














