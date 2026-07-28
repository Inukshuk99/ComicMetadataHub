"""
Comic Archive Writer Test
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


from src.exporters.comicrack.archive_writer import (
    ComicArchiveWriter
)


from src.importers.comicrack.archive_reader import (
    ComicArchiveReader
)



def test_archive_writer():

    print(
        "Testing comic archive writer..."
    )


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
            "page001.jpg",
            b"test"
        )


    writer = ComicArchiveWriter()


    writer.write(
        temp.name,
        b"""
        <ComicInfo>
            <Title>Batman</Title>
        </ComicInfo>
        """
    )


    reader = ComicArchiveReader()


    result = reader.read(
        temp.name
    )


    assert b"<Title>Batman</Title>" in result


    os.remove(
        temp.name
    )


    print(
        "Comic archive writer test passed"
    )



if __name__ == "__main__":

    test_archive_writer()
