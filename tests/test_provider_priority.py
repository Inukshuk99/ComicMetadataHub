"""
ComicMetadataHub Provider Priority Test
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


from src.hub.rules.provider_priority import (
    ProviderPriority
)



def test_provider_priority():

    print(
        "Testing provider priority..."
    )


    priority = ProviderPriority()


    assert priority.get_priority(
        "User"
    ) == 100


    assert priority.get_priority(
        "ComicVine"
    ) == 70


    assert priority.get_priority(
        "Unknown"
    ) == 0


    print(
        "Provider priority test passed"
    )



if __name__ == "__main__":

    test_provider_priority()
