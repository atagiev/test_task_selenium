from enum import Enum

from selenium.webdriver import Keys

WAIT_SLEEP_INTERVAL = 0.5
GAME_NAME = "StarCraft II"


class ScrollDirections(Enum):
    UP = Keys.PAGE_UP
    DOWN = Keys.PAGE_DOWN
