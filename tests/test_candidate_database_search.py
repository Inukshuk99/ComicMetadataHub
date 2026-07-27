"""
ComicMetadataHub Candidate Database Search Test
"""


import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from src.hub.matching.candidate_finder import (
    CandidateFinder
)


import sqlite3



def test_candidate_database_search():

    print(
        "Testing candidate database search..."
    )


    connection = sqlite3.connect(
        ":memory:"
    )

    connection.row_factory = sqlite3.Row


    cursor = connection.cursor()


    cursor.execute(
        """
        CREATE TABLE comicvine_series
        (
            id INTEGER,
            name TEXT
        )
        """
    )


    cursor.execute(
        """
        INSERT INTO comicvine_series
        VALUES
        (
            1,
            'Batman'
        )
        """
    )


    connection.commit()



    finder = CandidateFinder()


    results = finder.search_database(
        connection,
        "comicvine_series",
        "Batman"
    )


    assert len(results) == 1

    assert (
        results[0]["name"]
        ==
        "Batman"
    )


    connection.close()


    print(
        "Candidate database search test passed"
    )



if __name__ == "__main__":

    test_candidate_database_search()
