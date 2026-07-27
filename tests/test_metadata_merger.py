"""
ComicMetadataHub Metadata Merger Test
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



def test_metadata_merger():

    print(
        "Testing metadata merger..."
    )


    merger = MetadataMerger()


    existing = {

        "title": "Batman",

        "writer": "Bill Finger"

    }


    incoming = {

        "title": "Batman",

        "publisher": "DC",

        "writer": "Bill Finger, Bob Kane"

    }


    result = merger.merge(
        existing,
        incoming,
        "GCD"
    )


    assert result["data"]["publisher"] == (
        "DC"
    )


    assert result["data"]["title"] == (
        "Batman"
    )


    assert len(
        result["conflicts"]
    ) == 1


    assert result["conflicts"][0].field_name == (
        "writer"
    )


    print(
        "Metadata merger test passed"
    )



if __name__ == "__main__":

    test_metadata_merger()
