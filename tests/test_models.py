"""
ComicMetadataHub Model Test
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


from src.hub.models import (
    Publisher,
    Series,
    Volume,
    Issue,
    Edition,
    ComicFile,
    Creator,
    Identifier,
    IdentifierType,
)


def test_models():

    print(
        "Testing metadata models..."
    )


    publisher = Publisher(
        "DC Comics"
    )


    series = Series(
        "Batman",
        publisher
    )


    volume = Volume(
        "Batman v1",
        1940,
        2011
    )


    issue = Issue(
        "1",
        "The Legend of Batman"
    )


    edition = Edition(
        "Standard Edition"
    )


    comic_file = ComicFile(
        "Batman_001.cbz",
        "COMIC BOOKS/Batman/"
    )


    creator = Creator(
        "Bob Kane"
    )

    creator.add_role(
        "Creator"
    )


    identifier = Identifier(
        IdentifierType.COMIC_VINE,
        "4050-12345",
        "Comic Vine"
    )


    edition.files.append(
        comic_file
    )

    issue.editions.append(
        edition
    )

    issue.creators.append(
        creator
    )

    issue.identifiers.append(
        identifier
    )

    volume.issues.append(
        issue
    )

    series.volumes.append(
        volume
    )


    assert series.name == "Batman"
    assert volume.name == "Batman v1"
    assert issue.number == "1"
    assert edition.files[0].filename == "Batman_001.cbz"
    assert creator.roles[0].role == "Creator"
    assert identifier.value == "4050-12345"


    print(
        "Model test passed"
    )


if __name__ == "__main__":
    test_models()