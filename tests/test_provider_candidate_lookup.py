"""
ComicMetadataHub Provider Candidate Lookup Test
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


from src.hub.matching.candidate_finder import (
    CandidateFinder
)


from src.comicvine.database import (
    initialize_database as initialize_cv
)


from src.gcd.database import (
    initialize_database as initialize_gcd
)



def test_provider_candidate_lookup():

    print(
        "Testing provider candidate lookup..."
    )


    initialize_cv()

    initialize_gcd()


    finder = CandidateFinder()


    results = finder.find_provider_candidates(
        {
            "title": "Batman",
            "issue": "1"
        }
    )


    assert isinstance(
        results,
        list
    )


    print(
        "Provider candidate lookup test passed"
    )



if __name__ == "__main__":

    test_provider_candidate_lookup()
