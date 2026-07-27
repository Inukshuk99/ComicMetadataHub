"""
Comic Archive Reader Test
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


from src.importers.comicrack.archive_reader import (
    ComicArchiveReader
)



def test_archive_reader():

    print(
        "Testing comic archive reader..."
    )


    xml = """
    <ComicInfo>
        <Title>Test Batman</Title>
        <Series>Batman</Series>
        <Number>1</Number>
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


    reader = ComicArchiveReader()


    result = reader.read(
        temp.name
    )


    assert b"<Title>Test Batman</Title>" in result

    assert b"<Series>Batman</Series>" in result


    os.remove(
        temp.name
    )


    print(
        "Comic archive reader test passed"
    )



if __name__ == "__main__":

    test_archive_reader()