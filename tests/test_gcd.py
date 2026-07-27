"""
ComicMetadataHub GCD Provider Test
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


from src.gcd.provider import (
    GCDProvider
)



def test_gcd():

    print(
        "Testing GCD provider..."
    )


    provider = GCDProvider()


    assert provider.get_name() == (
        "GCD"
    )


    assert provider.can_process(
        "GCD"
    )


    result = provider.import_metadata(
        "GCD"
    )


    assert result.success

    assert result.source == (
        "GCD"
    )


    print(
        "GCD provider test passed"
    )



if __name__ == "__main__":

    test_gcd()
