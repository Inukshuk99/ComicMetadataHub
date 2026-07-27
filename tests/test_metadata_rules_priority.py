"""
ComicMetadataHub Metadata Rules Priority Test
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



def test_metadata_rules_priority():

    print(
        "Testing metadata rules priority..."
    )


    rules = MetadataRules()


    result = rules.compare(
        "writer",
        "Bob Kane",
        "Bill Finger",
        "ComicVine"
    )


    assert result["action"] == (
        "conflict"
    )


    assert result["source_priority"] == (
        70
    )


    print(
        "Metadata rules priority test passed"
    )



if __name__ == "__main__":

    test_metadata_rules_priority()
