"""
ComicMetadataHub Updater Framework Test
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


from src.updaters.base_updater import (
    BaseUpdater
)



def test_updaters():

    print(
        "Testing updater framework..."
    )


    assert (
        BaseUpdater.__abstractmethods__
    )


    assert (
        "update"
        in BaseUpdater.__abstractmethods__
    )


    print(
        "Updater framework test passed"
    )



if __name__ == "__main__":

    test_updaters()
