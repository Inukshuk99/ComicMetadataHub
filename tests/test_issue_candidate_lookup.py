"""
ComicMetadataHub Issue Candidate Lookup Test
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



def test_issue_candidate_lookup():

    print(
        "Testing issue candidate lookup..."
    )


    finder = CandidateFinder()


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


    results = finder.find_candidates(
        {
            "title": "Batman",
            "issue": "1"
        },
        candidates
    )


    assert len(results) == 1


    assert (
        results[0]["issue_number"]
        ==
        "1"
    )


    print(
        "Issue candidate lookup test passed"
    )



if __name__ == "__main__":

    test_issue_candidate_lookup()
