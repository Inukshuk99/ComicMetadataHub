"""
ComicRack Importer Test
"""


import sys
import os
import zipfile
import tempfile


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from src.importers.comicrack.importer import (
    ComicRackImporter
)



def test_comicrack_importer():

    print(
        "Testing ComicRack importer..."
    )


    xml = """
    <ComicInfo>
        <Title>Batman Test Issue</Title>
        <Series>Batman</Series>
        <Number>1</Number>
        <Writer>Bill Finger</Writer>
        <Publisher>DC Comics</Publisher>
        <Tags>CVDB105811</Tags>
    </ComicInfo>
    """


    temp = tempfile.NamedTemporaryFile(
        suffix=".cbz",
        delete=False
    )


    temp.close()


    with zipfile.ZipFile(
        temp.name,
        "w"
    ) as archive:

        archive.writestr(
            "ComicInfo.xml",
            xml
        )


    importer = ComicRackImporter()


    assert importer.can_import(
        temp.name
    )


    result = importer.import_metadata(
        temp.name
    )


    assert result["title"] == (
        "Batman Test Issue"
    )


    assert result["series"] == (
        "Batman"
    )


    assert result["identifiers"]["comicvine"] == (
        "105811"
    )


    os.remove(
        temp.name
    )


    print(
        "ComicRack importer test passed"
    )



if __name__ == "__main__":

    test_comicrack_importer()