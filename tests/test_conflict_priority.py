"""
ComicMetadataHub Conflict Priority Test
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


from src.hub.merge.conflict import (
    MetadataConflict
)


from src.hub.rules.provider_priority import (
    ProviderPriority
)



def test_conflict_priority():

    print(
        "Testing conflict priority..."
    )


    conflict = MetadataConflict(
        "writer"
    )


    conflict.add_value(
        "ComicRack",
        "Bob Kane"
    )


    conflict.add_value(
        "ComicVine",
        "Bill Finger"
    )


    conflict.add_value(
        "GCD",
        "Bill Finger"
    )


    winner = conflict.suggest_winner(
        ProviderPriority()
    )


    assert winner == (
        "ComicRack"
    )


    print(
        "Conflict priority test passed"
    )



if __name__ == "__main__":

    test_conflict_priority()
