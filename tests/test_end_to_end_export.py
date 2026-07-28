"""
ComicMetadataHub End To End Export Test
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


from src.importers.comicrack.reader import (
    ComicInfoReader
)


from src.importers.comicrack.mapper import (
    ComicRackMapper
)


from src.services.export_service import (
    ExportService
)



def test_end_to_end_export():

    print(
        "Testing end to end export..."
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
            "ComicInfo.xml",
            """
            <ComicInfo>
                <Title>Batman</Title>
                <Series>Batman</Series>
                <Number>1</Number>
            </ComicInfo>
            """
        )


    xml = ComicArchiveReader().read(
        temp.name
    )


    root = __import__(
        "xml.etree.ElementTree",
        fromlist=["ElementTree"]
    ).fromstring(
        xml
    )


    raw = ComicInfoReader().read_xml(
        root
    )


    metadata = ComicRackMapper().map(
        raw
    )


    metadata["publisher"] = "DC Comics"


    ExportService().export_comicinfo(
        temp.name,
        metadata
    )


    updated = ComicArchiveReader().read(
        temp.name
    )


    assert b"<Title>Batman</Title>" in updated

    assert b"<Publisher>DC Comics</Publisher>" in updated


    os.remove(
        temp.name
    )


    print(
        "End to end export test passed"
    )



if __name__ == "__main__":

    test_end_to_end_export()
