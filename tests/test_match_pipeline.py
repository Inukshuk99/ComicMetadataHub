"""
ComicMetadataHub Match Pipeline Test
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


from src.hub.matching.match_pipeline import (
    MatchPipeline
)



def test_match_pipeline():

    print(
        "Testing match pipeline..."
    )


    pipeline = MatchPipeline()


    record = {

        "title": "Batman",

        "issue": "1",

        "publisher": "DC",

        "year": 1940

    }



    candidates = [

        {

            "title": "Batman",

            "issue_number": "1",

            "publisher": "DC",

            "year": 1940

        },

        {

            "title": "Batman",

            "issue_number": "2",

            "publisher": "DC",

            "year": 1940

        }

    ]



    results = pipeline.match(
        record,
        candidates
    )


    assert len(results) == 2


    assert (
        results[0]["rank_score"]
        >=
        results[1]["rank_score"]
    )


    print(
        "Match pipeline test passed"
    )



if __name__ == "__main__":

    test_match_pipeline()
