"""
ComicMetadataHub GCD Database Test
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


from src.gcd.database import (
    initialize_database,
    get_connection
)



def test_gcd_database():

    print(
        "Testing GCD database..."
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
        "gcd_issues"
        in tables
    )


    assert (
        "gcd_series"
        in tables
    )


    connection.close()


    print(
        "GCD database test passed"
    )



if __name__ == "__main__":

    test_gcd_database()
