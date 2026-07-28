"""
ComicVine Client Test
"""

import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from src.comicvine.client import (
    ComicVineClient
)



def test_comicvine_client():

    print(
        "Testing ComicVine client..."
    )


    client = ComicVineClient()


    assert client.BASE_URL == (
        "https://comicvine.gamespot.com/api"
    )


    assert client.is_configured() in (
        True,
        False
    )


    if not client.is_configured():

        try:

            client.request(
                "/test"
            )

            assert False

        except RuntimeError:

            pass


    print(
        "ComicVine client test passed"
    )



if __name__ == "__main__":

    test_comicvine_client()
