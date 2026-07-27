"""
ComicMetadataHub Database Updater Test
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


from src.updaters.database_updater import (
    DatabaseUpdater
)



def test_database_updater():

    print(
        "Testing database updater..."
    )


    updater = DatabaseUpdater()


    assert hasattr(
        updater,
        "insert_records"
    )


    print(
        "Database updater test passed"
    )



if __name__ == "__main__":

    test_database_updater()
