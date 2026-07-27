"""
ComicMetadataHub Creator Merger Test
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


from src.hub.merge.creator_merger import (
    CreatorMerger
)


from src.hub.models.creator import (
    Creator
)



def test_creator_merger():

    print(
        "Testing creator merger..."
    )


    merger = CreatorMerger()


    bill = Creator(
        "Bill Finger"
    )

    bill.add_role(
        "Writer"
    )


    existing = [
        bill
    ]


    incoming_bill = Creator(
        "Bill Finger"
    )

    incoming_bill.add_role(
        "Writer"
    )


    bob = Creator(
        "Bob Kane"
    )

    bob.add_role(
        "Penciller"
    )


    incoming = [
        incoming_bill,
        bob
    ]


    result = merger.merge(
        existing,
        incoming
    )


    assert len(result) == 2


    assert result[0].name == (
        "Bill Finger"
    )


    assert len(
        result[0].roles
    ) == 1


    assert result[1].name == (
        "Bob Kane"
    )


    assert result[1].roles[0].role == (
        "Penciller"
    )


    print(
        "Creator merger test passed"
    )



if __name__ == "__main__":

    test_creator_merger()
