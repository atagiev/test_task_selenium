from typing import Callable


def url(page_url: str) -> Callable:
    """
    Decorator for web pages, is used to specify the url of the page more nicely
    """
    def decorator(cls):
        setattr(cls, '_url', page_url)
        return cls

    return decorator
