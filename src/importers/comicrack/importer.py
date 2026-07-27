"""
ComicRack Importer

Imports metadata from standard comic archives:

.cbz
.zip
.cbr

using ComicInfo.xml.
"""


import xml.etree.ElementTree as ET


from src.importers.base_importer import (
    BaseImporter
)


from src.importers.metadata_result import (
    MetadataResult
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



class ComicRackImporter(BaseImporter):
    """
    ComicRack compatible importer.
    """


    name = "ComicRack"



    def __init__(self):

        self.archive_reader = ComicArchiveReader()

        self.xml_reader = ComicInfoReader()

        self.mapper = ComicRackMapper()



    def can_import(
        self,
        filename
    ):
        """
        Check if file format is supported.
        """

        filename = filename.lower()


        return filename.endswith(
            (
                ".cbz",
                ".zip",
                ".cbr",
            )
        )



    def import_metadata(
        self,
        filename
    ):
        """
        Import metadata from comic archive.
        """

        if not self.can_import(
            filename
        ):

            raise ValueError(
                "Unsupported comic format"
            )


        xml_data = self.archive_reader.read(
            filename
        )


        root = ET.fromstring(
            xml_data
        )


        comicinfo = self.xml_reader.read_xml(
            root
        )


        metadata = self.mapper.map(
            comicinfo
        )


        return MetadataResult(
            source="ComicRack",
            data=metadata
        )