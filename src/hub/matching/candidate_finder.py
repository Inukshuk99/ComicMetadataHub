"""
ComicMetadataHub Candidate Finder

Finds possible comic records from
provider databases.

Candidate discovery only.
Final decisions are handled by
ranking and identity resolution.
"""


from src.comicvine.database import (
    get_connection as get_comicvine_connection
)


from src.gcd.database import (
    get_connection as get_gcd_connection
)



class CandidateFinder:
    """
    Finds possible comic candidates.
    """



    def find_candidates(
        self,
        record,
        candidates
    ):
        """
        Return supplied candidates.

        CandidateFinder does not decide
        the final match.
        """

        return list(candidates)



    def search_database(
        self,
        connection,
        table,
        field_or_value,
        value=None
    ):
        """
        Generic database search helper.
        """


        cursor = connection.cursor()


        if value is None:

            cursor.execute(
                f"""
                SELECT *
                FROM {table}
                WHERE name = ?
                """,
                (
                    field_or_value,
                )
            )

        else:

            cursor.execute(
                f"""
                SELECT *
                FROM {table}
                WHERE {field_or_value} = ?
                """,
                (
                    value,
                )
            )


        return [
            dict(row)
            for row in cursor.fetchall()
        ]



    def search_comicvine(
        self,
        record
    ):

        connection = get_comicvine_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT
                comicvine_issues.id,
                comicvine_issues.comicvine_id,
                comicvine_series.name AS title,
                comicvine_issues.issue_number,
                comicvine_issues.title AS issue_title,
                comicvine_issues.year,
                'ComicVine' AS source

            FROM comicvine_issues

            JOIN comicvine_series

            ON comicvine_issues.series_id =
               comicvine_series.id

            WHERE comicvine_series.name = ?
            """,
            (
                record.get("title"),
            )
        )


        results = [
            dict(row)
            for row in cursor.fetchall()
        ]


        connection.close()


        return results



    def search_gcd(
        self,
        record
    ):

        connection = get_gcd_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT
                gcd_issues.id,
                gcd_issues.gcd_id,
                gcd_series.name AS title,
                gcd_issues.issue_number,
                gcd_issues.title AS issue_title,
                gcd_issues.year,
                'GCD' AS source

            FROM gcd_issues

            JOIN gcd_series

            ON gcd_issues.series_id =
               gcd_series.id

            WHERE gcd_series.name = ?
            """,
            (
                record.get("title"),
            )
        )


        results = [
            dict(row)
            for row in cursor.fetchall()
        ]


        connection.close()


        return results



    def find_provider_candidates(
        self,
        record
    ):
        """
        Collect candidates from providers.
        """


        results = []


        results.extend(
            self.search_comicvine(
                record
            )
        )


        results.extend(
            self.search_gcd(
                record
            )
        )


        return results
