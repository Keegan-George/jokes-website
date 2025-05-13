"""
Contains a single function for retrieving two-part jokes from the JokeAPI.
"""

import requests

JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"

BLACK_LIST_FLAGS = ["nsfw", "religious", "political", "racist", "sexist", "explicit"]

PARAMS = {"type": "twopart", "blacklistFlags": ",".join(BLACK_LIST_FLAGS)}


def get_joke() -> tuple[str, str]:
    """retrieves a two-part joke"""

    response = requests.get(url=JOKE_API_URL, params=PARAMS)
    joke = response.json()
    return (joke["setup"], joke["delivery"])
