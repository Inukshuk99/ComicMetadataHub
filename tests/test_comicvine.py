"""
ComicMetadataHub ComicVine Provider Test
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


from src.comicvine.provider import (
    ComicVineProvider
)



def test_comicvine():

    print(
        "Testing ComicVine provider..."
    )


    provider = ComicVineProvider()


    assert provider.get_name() == (
        "ComicVine"
    )


    assert provider.can_process(
        "ComicVine"
    )


    result = provider.import_metadata(
        "ComicVine"
    )


    assert result.success

    assert result.source == (
        "ComicVine"
    )


    print(
        "ComicVine provider test passed"
    )



if __name__ == "__main__":

    test_comicvine()