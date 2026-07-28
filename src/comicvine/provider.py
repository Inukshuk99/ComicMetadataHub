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



    def search_series(
        self,
        query
    ):
        """
        Search ComicVine volumes.
        """

        response = self.client.search(
            query,
            "volume"
        )


        results = []


        for record in response.get(
            "results",
            []
        ):

            results.append(
                self.mapper.map_series(
                    record
                )
            )


        return results



    def search_issues(
        self,
        query
    ):
        """
        Search ComicVine issues.
        """

        response = self.client.search(
            query,
            "issue"
        )


        results = []


        for record in response.get(
            "results",
            []
        ):

            results.append(
                self.mapper.map_issue(
                    record
                )
            )


        return results



    def get_series(
        self,
        series_id
    ):

        response = self.client.get_volume(
            series_id
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

        response = self.client.get_issue(
            issue_id
        )


        return self.mapper.map_issue(
            response.get(
                "results",
                {}
            )
        )
