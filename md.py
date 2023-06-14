import sys

query = "{query}"

import os
from mastodon import Mastodon


def toot(message):
    Mastodon(
        access_token = os.environ['MASTODON_TOKEN'],
        api_base_url = os.environ['MASTODON_URL']
    ).toot(message)

if __name__ == "__main__":
    toot(query)
