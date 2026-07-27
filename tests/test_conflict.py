"""
ComicMetadataHub Metadata Conflict Test
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



def test_conflict():

    print(
        "Testing metadata conflict model..."
    )


    conflict = MetadataConflict(
        "writer"
    )


    conflict.add_value(
        "ComicRack",
        "Bill Finger"
    )


    conflict.add_value(
        "ComicVine",
        "Bill Finger"
    )


    conflict.add_value(
        "GCD",
        "Bill Finger, Bob Kane"
    )


    assert conflict.field_name == (
        "writer"
    )


    assert conflict.values[
        "ComicRack"
    ] == (
        "Bill Finger"
    )


    assert conflict.values[
        "GCD"
    ] == (
        "Bill Finger, Bob Kane"
    )


    assert not conflict.resolved


    conflict.resolve(
        "ComicVine"
    )


    assert conflict.resolved


    assert conflict.selected_source == (
        "ComicVine"
    )


    print(
        "Metadata conflict model test passed"
    )



if __name__ == "__main__":

    test_conflict()
