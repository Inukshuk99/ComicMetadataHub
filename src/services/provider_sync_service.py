"""
ComicMetadataHub Provider Sync Service

Coordinates provider data updates
into local provider databases.
"""



class ProviderSyncService:
    """
    Synchronizes normalized provider
    records using provider updaters.
    """



    def sync(
        self,
        records,
        updater
    ):
        """
        Send normalized records to updater.
        """

        if records is None:

            records = []


        return updater.update(
            records
        )
