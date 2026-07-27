"""
ComicMetadataHub GCD Provider

Provides Grand Comics Database metadata integration.

Initial implementation:
- Defines GCD source provider
- Returns MetadataResult structure
- No API communication yet
"""


from src.importers.metadata_result import (
    MetadataResult
)



class GCDProvider:
    """
    Grand Comics Database metadata provider.
    """


    name = "GCD"



    def can_process(
        self,
        source
    ):
        """
        Determine if this provider
        can process the supplied source.
        """

        return source == "GCD"



    def get_name(
        self
    ):
        """
        Return provider name.
        """

        return self.name



    def import_metadata(
        self,
        source
    ):
        """
        Import GCD metadata.

        Placeholder until integration
        is implemented.
        """

        if not self.can_process(
            source
        ):

            return MetadataResult(
                source=self.name,
                success=False,
                errors=[
                    "Unsupported source"
                ]
            )


        return MetadataResult(
            source=self.name,
            data={}
        )
