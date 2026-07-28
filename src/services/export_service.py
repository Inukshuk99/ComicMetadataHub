"""
ComicMetadataHub Export Service

Handles exporting normalized metadata
back into comic archives.
"""


from src.exporters.comicrack.writer import (
    ComicInfoWriter
)


from src.exporters.comicrack.archive_writer import (
    ComicArchiveWriter
)



class ExportService:
    """
    Coordinates metadata export.
    """



    def __init__(self):

        self.writer = ComicInfoWriter()

        self.archive_writer = ComicArchiveWriter()



    def export_comicinfo(
        self,
        filename,
        metadata
    ):
        """
        Write metadata into comic archive.
        """


        xml = self.writer.write(
            metadata
        )


        return self.archive_writer.write(
            filename,
            xml
        )
