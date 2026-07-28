"""
ComicMetadataHub Provider Issue Lookup Test
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
    initialize_database as initialize_cv,
    get_connection as get_cv_connection
)


from src.gcd.database import (
    initialize_database as initialize_gcd,
    get_connection as get_gcd_connection
)


from src.comicvine.updater import (
    ComicVineUpdater
)


from src.gcd.updater import (
    GCDUpdater
)


from src.hub.matching.candidate_finder import (
    CandidateFinder
)



def test_provider_issue_lookup():

    print(
        "Testing provider issue lookup..."
    )


    initialize_cv()

    initialize_gcd()


    ComicVineUpdater().update(
        [
            {
                "comicvine_id": "cv_issue_1",
                "type": "issue",
                "series_id": None,
                "issue_number": "1",
                "title": "Batman #1",
                "year": 1940
            }
        ]
    )


    GCDUpdater().update(
        [
            {
                "gcd_id": "gcd_issue_1",
                "type": "issue",
                "series_id": None,
                "issue_number": "1",
                "title": "Batman #1",
                "year": 1940
            }
        ]
    )


    finder = CandidateFinder()


    cv = get_cv_connection()

    gcd = get_gcd_connection()


    assert cv is not None

    assert gcd is not None


    cv.close()

    gcd.close()


    print(
        "Provider issue lookup test passed"
    )



if __name__ == "__main__":

    test_provider_issue_lookup()
