"""
ComicMetadataHub ComicVine Mapper

Converts ComicVine API records
into normalized ComicMetadataHub metadata.
"""


class ComicVineMapper:
    """
    Maps ComicVine records.
    """



    def map_series(
        self,
        record
    ):
        """
        Convert ComicVine series record.
        """

        return {

            "type": "series",

            "comicvine_id": record.get(
                "id"
            ),

            "name": record.get(
                "name"
            ),

            "start_year": record.get(
                "start_year"
            ),

            "end_year": record.get(
                "end_year"
            )

        }



    def map_issue(
        self,
        record
    ):
        """
        Convert ComicVine issue record.
        """

        return {

            "type": "issue",

            "comicvine_id": record.get(
                "id"
            ),

            "series_id": (
                record.get(
                    "volume",
                    {}
                )
                .get(
                    "id"
                )
            ),

            "issue_number": record.get(
                "issue_number"
            ),

            "title": record.get(
                "name"
            ),

            "year": self._extract_year(
                record.get(
                    "cover_date"
                )
            )

        }



    def map_publisher(
        self,
        record
    ):
        """
        Convert ComicVine publisher record.
        """

        return {

            "type": "publisher",

            "comicvine_id": record.get(
                "id"
            ),

            "name": record.get(
                "name"
            )

        }



    def map_creator(
        self,
        record
    ):
        """
        Convert ComicVine creator record.
        """

        return {

            "type": "creator",

            "comicvine_id": record.get(
                "id"
            ),

            "name": record.get(
                "name"
            )

        }



    def _extract_year(
        self,
        value
    ):

        if not value:

            return None


        return str(
            value
        )[0:4]
