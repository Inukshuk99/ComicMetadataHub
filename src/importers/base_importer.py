"""
ComicMetadataHub Base Importer

Defines the interface that all metadata
importers must follow.
"""


from abc import ABC, abstractmethod


class BaseImporter(ABC):
    """
    Base class for all metadata importers.
    """


    name = "Unknown"


    @abstractmethod
    def can_import(self, source):
        """
        Determine whether this importer
        can process the supplied source.

        Example:
            file type
            application data
            API response
        """

        pass


    @abstractmethod
    def import_metadata(self, source):
        """
        Import metadata from a source.

        Returns normalized raw metadata.
        """

        pass


    def get_name(self):
        """
        Return importer name.
        """

        return self.name