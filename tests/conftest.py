import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1366
    yield
    browser.quit()
