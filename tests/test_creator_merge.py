"""
ComicMetadataHub Creator Merge Test
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



def test_creator_merge():

    print(
        "Testing creator merge..."
    )


    merger = MetadataMerger()


    existing = {

        "writer": "Bob Kane"

    }


    incoming = {

        "writer": "Bill Finger"

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
        "writer"
    )


    assert decision["rule"] == (
        "conflict"
    )


    print(
        "Creator merge test passed"
    )



if __name__ == "__main__":

    test_creator_merge()
