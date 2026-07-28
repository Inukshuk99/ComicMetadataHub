"""
ComicMetadataHub ComicVine Provider

Provides ComicVine metadata integration.
"""


from src.importers.metadata_result import (
    MetadataResult
)


from src.comicvine.client import (
    ComicVineClient
)


from src.comicvine.mapper import (
    ComicVineMapper
)



class ComicVineProvider:
    """
    ComicVine metadata provider.
    """


    name = "ComicVine"



    def __init__(
        self
    ):

        self.client = ComicVineClient()

        self.mapper = ComicVineMapper()



    def can_process(
        self,
        source
    ):

        return source == self.name



    def get_name(
        self
    ):

        return self.name



    def import_metadata(
        self,
        source
    ):

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


        result = MetadataResult(
            source=self.name,
            data={}
        )


        if not self.client.is_configured():

            result.add_warning(
                "COMICVINE_API_KEY is not configured"
            )


        return result



    def get_series(
        self,
        series_id
    ):

        response = self.client.request(
            "/volume/4025-"
            + str(series_id)
            + "/"
        )


        return self.mapper.map_series(
            response.get(
                "results",
                {}
            )
        )



    def get_issue(
        self,
        issue_id
    ):

        response = self.client.request(
            "/issue/4000-"
            + str(issue_id)
            + "/"
        )


        return self.mapper.map_issue(
            response.get(
                "results",
                {}
            )
        )
