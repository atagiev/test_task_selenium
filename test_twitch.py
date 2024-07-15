import random

from utils.constants import GAME_NAME, ScrollDirections


def test_twitch(twitch_page):
    twitch_page.find_game_in_twitch(GAME_NAME)

    twitch_page.scroll_page(ScrollDirections.DOWN, 2)

    streamers = twitch_page.get_twitch_streamers_on_page()

    assert streamers, 'No streamers found on the page'

    random_streamer = random.choice(streamers)
    random_streamer.click()

    twitch_page.close_popup_window()

    twitch_page.wait_until_stream_loads()

    twitch_page.take_screenshot()
