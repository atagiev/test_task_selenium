import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
import selenium

from pages.TwitchPage import TwitchPage


@pytest.fixture(scope='module')
def webdriver() -> WebDriver:
    mobile_emulation = {
        "deviceName": "Pixel 2"
    }
    driver = None
    try:
        chrome_options = selenium.webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        driver = selenium.webdriver.Chrome(options=chrome_options)
        yield driver
    finally:
        if driver:
            driver.quit()


@pytest.fixture(scope='function')
def twitch_page(webdriver) -> TwitchPage:
    page = TwitchPage(driver=webdriver)
    page.open()
    yield page
