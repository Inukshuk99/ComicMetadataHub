"""
ComicMetadataHub Candidate Provider Search Test
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



def test_candidate_provider_search():

    print(
        "Testing candidate provider search..."
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

            "source": "ComicVine"

        },

        {

            "title": "Batman",

            "issue_number": "2",

            "source": "ComicVine"

        },

        {

            "title": "Superman",

            "issue_number": "1",

            "source": "GCD"

        }

    ]


    result = finder.find_candidates(
        record,
        candidates
    )


    assert len(result) == 1


    assert (
        result[0]["source"]
        ==
        "ComicVine"
    )


    print(
        "Candidate provider search test passed"
    )



if __name__ == "__main__":

    test_candidate_provider_search()
