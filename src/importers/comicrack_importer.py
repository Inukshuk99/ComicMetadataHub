"""
ComicMetadataHub ComicRack Importer

Initial implementation stub.
"""

from .base_importer import BaseImporter
from .metadata_result import MetadataResult


class ComicRackImporter(BaseImporter):

    name = "ComicRack"


    def can_import(
        self,
        source
    ):
        """
        Determine whether source
        is supported by ComicRack importer.
        """

        return True


    def import_metadata(
        self,
        source
    ):
        """
        Initial placeholder importer.

        Real ComicRack metadata extraction
        will be added later.
        """

        return MetadataResult(
            source=self.name,
            data={}
        )