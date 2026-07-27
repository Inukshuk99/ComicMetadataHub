"""
ComicMetadataHub ComicVine Database Test
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


from src.comicvine.database import (
    initialize_database,
    get_connection
)



def test_comicvine_database():

    print(
        "Testing ComicVine database..."
    )


    initialize_database()


    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)


    tables = [

        row["name"]

        for row in cursor.fetchall()

    ]


    assert (
        "comicvine_issues"
        in tables
    )


    assert (
        "comicvine_series"
        in tables
    )


    connection.close()


    print(
        "ComicVine database test passed"
    )



if __name__ == "__main__":

    test_comicvine_database()
