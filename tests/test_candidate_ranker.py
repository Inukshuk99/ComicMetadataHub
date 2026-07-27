"""
ComicMetadataHub Candidate Ranker Test
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


from src.hub.matching.candidate_ranker import (
    CandidateRanker
)



def test_candidate_ranker():

    print(
        "Testing candidate ranker..."
    )


    ranker = CandidateRanker()


    source = {
        "title": "Batman",
        "issue": "1",
        "publisher": "DC",
        "year": 1940
    }


    candidates = [

        {
            "title": "Batman",
            "issue": "1",
            "publisher": "DC",
            "year": 1940
        },

        {
            "title": "Batman",
            "issue": "1",
            "publisher": "DC",
            "year": 2011
        }

    ]


    results = ranker.rank(
        source,
        candidates
    )


    assert results[0][0] > results[1][0]


    print(
        "Candidate ranker test passed"
    )



if __name__ == "__main__":

    test_candidate_ranker()
