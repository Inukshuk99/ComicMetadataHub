"""
ComicMetadataHub Base Updater

Defines the interface for source
database update operations.
"""


from abc import ABC, abstractmethod



class BaseUpdater(ABC):
    """
    Base class for metadata updaters.
    """



    name = "Unknown"



    @abstractmethod
    def update(self):
        """
        Update local source database.
        """

        pass



    def get_name(self):

        return self.name
