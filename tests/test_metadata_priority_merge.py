"""
ComicMetadataHub Metadata Priority Merge Test
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



def test_metadata_priority_merge():

    print(
        "Testing metadata priority merge..."
    )


    merger = MetadataMerger()


    existing = {

        "publisher": "Unknown"

    }


    incoming = {

        "publisher": "DC"

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
        "publisher"
    )


    assert decision["rule"] == (
        "priority"
    )


    assert decision["suggested_source"] == (
        "ComicVine"
    )


    assert decision["suggested_value"] == (
        "DC"
    )


    print(
        "Metadata priority merge test passed"
    )



if __name__ == "__main__":

    test_metadata_priority_merge()
