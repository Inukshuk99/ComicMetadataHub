"""
ComicMetadataHub Metadata Rules Test
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


from src.hub.rules.metadata_rules import (
    MetadataRules
)



def test_metadata_rules():

    print(
        "Testing metadata rules..."
    )


    rules = MetadataRules()


    # Empty field fills

    result = rules.compare(
        "writer",
        "",
        "Bill Finger",
        "ComicVine"
    )


    assert result["action"] == (
        "fill"
    )


    # Same value accepts

    result = rules.compare(
        "writer",
        "Bill Finger",
        "Bill Finger",
        "ComicVine"
    )


    assert result["action"] == (
        "accept"
    )


    # Different value creates conflict

    result = rules.compare(
        "writer",
        "Bill Finger",
        "Bill Finger, Bob Kane",
        "GCD"
    )


    assert result["action"] == (
        "conflict"
    )


    assert result["conflict"].field_name == (
        "writer"
    )


    print(
        "Metadata rules test passed"
    )



if __name__ == "__main__":

    test_metadata_rules()
