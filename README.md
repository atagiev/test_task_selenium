To start, run the command `pip install -r requirements.txt` and then `pytest test_twitch.py`.

Pytest is used to run the tests. The fixtures used in the tests are located in the conftest.py file. The utils folder contains necessary constants and helper functions.

In the pages folder, there is a base class for describing a web page in Selenium, as well as a specific class for working with the Twitch page.