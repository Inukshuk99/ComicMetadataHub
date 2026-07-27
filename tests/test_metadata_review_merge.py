"""
ComicMetadataHub Metadata Review Merge Test
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


from src.hub.merge.metadata_merger import (
    MetadataMerger
)



def test_metadata_review_merge():

    print(
        "Testing metadata review merge..."
    )


    merger = MetadataMerger()


    existing = {

        "title": "Batman"

    }


    incoming = {

        "title": "The Batman"

    }


    result = merger.merge(
        existing,
        incoming,
        "ComicVine"
    )


    assert len(
        result["conflicts"]
    ) == 1


    decision = result["decisions"][0]


    assert decision["field"] == (
        "title"
    )


    assert decision["rule"] == (
        "review"
    )


    assert decision["requires_review"]



    print(
        "Metadata review merge test passed"
    )



if __name__ == "__main__":

    test_metadata_review_merge()
