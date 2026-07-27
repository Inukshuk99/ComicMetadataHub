"""
ComicMetadataHub GCD Updater Test
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


from src.gcd.updater import (
    GCDUpdater
)


from src.gcd.database import (
    initialize_database,
    get_connection
)



def test_gcd_updater():

    print(
        "Testing GCD updater..."
    )


    initialize_database()


    updater = GCDUpdater()


    count = updater.update(
        [
            {
                "gcd_id": "98765",
                "name": "Batman",
                "start_year": 1940,
                "end_year": None
            }
        ]
    )


    assert count == 1



    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM gcd_series
        WHERE gcd_id = '98765'
        """
    )


    result = cursor.fetchone()


    assert result["name"] == (
        "Batman"
    )


    connection.close()


    print(
        "GCD updater test passed"
    )



if __name__ == "__main__":

    test_gcd_updater()
