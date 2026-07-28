"""
ComicMetadataHub Match Pipeline Merge Test
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



def test_match_pipeline_merge():

    print(
        "Testing match pipeline merge..."
    )


    pipeline = MatchPipeline()


    record = {

        "title": "Batman",

        "series": "Batman",

        "issue": "1",

        "publisher": "DC",

        "identifiers": {

            "comicvine": "105811"

        }

    }


    candidates = [

        {

            "title": "Batman",

            "series": "Batman",

            "issue": "1",

            "publisher": "DC",

            "metadata_provider": "ComicVine",

            "identifiers": {

                "comicvine": "105811"

            }

        }

    ]


    results = pipeline.match(
        record,
        candidates
    )


    assert results[0]["match"].matched


    assert results[0]["merged"] is not None


    assert results[0]["merged"]["data"]["title"] == (
        "Batman"
    )


    print(
        "Match pipeline merge test passed"
    )



if __name__ == "__main__":

    test_match_pipeline_merge()
