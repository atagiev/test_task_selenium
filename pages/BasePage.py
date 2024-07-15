import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import ScrollDirections, WAIT_SLEEP_INTERVAL


class BasePage:
    def __init__(self, driver: WebDriver, url: str | None = None):
        self._driver = driver
        if url is not None:
            self._url = url

    @property
    def driver(self) -> WebDriver:
        return self._driver

    @property
    def url(self) -> str:
        if not hasattr(self, '_url'):
            raise ValueError('Page url should be provided')
        if not self._url:
            raise ValueError('Page url should be valid')
        return self._url

    def open(self) -> None:
        """
        Open web page
        """
        page_url = self.url
        self.driver.get(page_url)

    def scroll_page(self, direction: ScrollDirections, scroll_amount: int) -> None:
        """
        Scroll web page using keyboard
        :param direction: UP or DOWN
        :param scroll_amount: Number of scroll key presses
        """
        body = self.driver.find_element(By.TAG_NAME, 'body')
        for _ in range(scroll_amount):
            body.send_keys(direction.value)
            time.sleep(WAIT_SLEEP_INTERVAL)  # Wait for the page to load after each scroll

    def take_screenshot(self, file_name: str = 'screenshot.png') -> None:
        """
        Save screenshot of the page
        :param file_name: Screenshot name
        """
        self.driver.save_screenshot(file_name)

    def wait_for_element(self, by: str, value: str, timeout: int = 10) -> WebElement:
        """
        Wait for web element to load
        :param by: used to find the element
        :param value: used to find the element
        :param timeout: loading timeout
        :return: web element
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def find_element_and_click(self, by: str, value: str) -> None:
        """
        Wait for web element to load and click it
        :param by: used to find the element
        :param value: used to find the element
        """
        element = self.wait_for_element(by, value)
        element.click()

    def enter_value_to_element(self, by: str, value: str, data_to_input: str) -> None:
        """
        Wait for element to load, input some text into text field and press ENTER
        :param by: used to find the element
        :param value: used to find the element
        :param data_to_input: text to input
        """
        element = self.wait_for_element(by, value)
        element.send_keys(data_to_input)
        element.send_keys(Keys.ENTER)

    def find_elements(self, by: str, value: str) -> list[WebElement]:
        """
        Find elements on page by locator
        :param by: used to find the element
        :param value: used to find the element
        :return: list of web elements
        """
        self.wait_for_element(by, value)
        elements = self.driver.find_elements(by, value)
        return elements
