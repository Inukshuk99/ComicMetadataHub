"""
ComicMetadataHub ComicVine Updater Test
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


from src.comicvine.updater import (
    ComicVineUpdater
)


from src.comicvine.database import (
    initialize_database,
    get_connection
)



def test_comicvine_updater():

    print(
        "Testing ComicVine updater..."
    )


    initialize_database()


    updater = ComicVineUpdater()


    count = updater.update(
        [
            {
                "comicvine_id": "12345",
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
        FROM comicvine_series
        WHERE comicvine_id = '12345'
        """
    )


    result = cursor.fetchone()


    assert result["name"] == (
        "Batman"
    )


    connection.close()


    print(
        "ComicVine updater test passed"
    )



if __name__ == "__main__":

    test_comicvine_updater()
