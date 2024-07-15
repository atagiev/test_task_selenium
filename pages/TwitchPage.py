from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.BasePage import BasePage
from utils.decorators import url


@url('https://www.twitch.tv')
class TwitchPage(BasePage):

    def find_game_in_twitch(self, game_name: str) -> None:
        """
        Finds a game by its name in the search box on twich
        :param game_name: Name of the game
        """
        # Click search button
        self.find_element_and_click(By.CSS_SELECTOR, 'a[aria-label="Search"]')

        # Search for game
        self.enter_value_to_element(By.CSS_SELECTOR, 'input[data-a-target="tw-input"]', data_to_input=game_name)

    def get_twitch_streamers_on_page(self) -> list[WebElement]:
        """
        Gets the list of streams on the current page.
        A stream is defined as having a preview image and a "Live" icon inside it
        :return: list of twitch streamers
        """
        elements = self.find_elements(By.CSS_SELECTOR, "a[class*='ScCoreLink'][class*='tw-link']")

        streamers = []

        for element in elements:
            try:
                # Trying to find streamer preview inside element
                element.find_element(By.XPATH, ".//img")
                element.find_element(By.CSS_SELECTOR, 'div[class*="tw-channel-status-text-indicator"')
                streamers.append(element)
            except:
                continue

        return streamers

    def close_popup_window(self) -> None:
        """
        Closes pop-up window on stream if it exists
        """
        try:
            self.find_element_and_click(By.CSS_SELECTOR,
                                        'button[data-a-target="content-classification-gate-overlay-start-watching-button"]')
        except:
            pass

    def wait_until_stream_loads(self):
        """
        Wait until stream content loads
        """
        self.wait_for_element(By.CSS_SELECTOR, 'div[data-a-target="player-overlay-click-handler"]')
