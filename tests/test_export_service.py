"""
ComicMetadataHub Export Service Test
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


from src.services.export_service import (
    ExportService
)


from src.importers.comicrack.archive_reader import (
    ComicArchiveReader
)



def test_export_service():

    print(
        "Testing export service..."
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


    service = ExportService()


    service.export_comicinfo(
        temp.name,
        {
            "title": "Batman",
            "series": "Batman",
            "issue": "1",
            "publisher": "DC"
        }
    )


    xml = ComicArchiveReader().read(
        temp.name
    )


    assert b"<Title>Batman</Title>" in xml

    assert b"<Series>Batman</Series>" in xml


    os.remove(
        temp.name
    )


    print(
        "Export service test passed"
    )



if __name__ == "__main__":

    test_export_service()
