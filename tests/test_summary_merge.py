"""
ComicMetadataHub Summary Merge Test
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



def test_summary_merge():

    print(
        "Testing summary merge..."
    )


    merger = MetadataMerger()


    existing = {

        "summary": "Batman fights crime."

    }


    incoming = {

        "summary": (
            "Batman fights crime in Gotham City "
            "while facing dangerous enemies and "
            "protecting the innocent."
        )

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
        "summary"
    )


    assert decision["rule"] == (
        "prefer_complete"
    )


    assert decision["suggested_source"] == (
        "ComicVine"
    )


    assert decision["suggested_value"] == (
        incoming["summary"]
    )


    print(
        "Summary merge test passed"
    )



if __name__ == "__main__":

    test_summary_merge()
