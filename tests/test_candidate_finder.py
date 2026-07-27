"""
ComicMetadataHub Candidate Finder Test
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



def test_candidate_finder():

    print(
        "Testing candidate finder..."
    )


    finder = CandidateFinder()


    record = {

        "title": "Batman",

        "issue": "1"

    }


    candidates = [

        {

            "title": "Batman",

            "issue_number": "1",

            "year": 1940

        },

        {

            "title": "Batman",

            "issue_number": "2",

            "year": 1940

        }

    ]


    results = finder.find_candidates(
        record,
        candidates
    )


    #
    # CandidateFinder discovers candidates.
    # It does not select the winner.
    #

    assert len(results) == 2


    assert results[0]["title"] == "Batman"

    assert results[1]["title"] == "Batman"


    print(
        "Candidate finder test passed"
    )



if __name__ == "__main__":

    test_candidate_finder()
