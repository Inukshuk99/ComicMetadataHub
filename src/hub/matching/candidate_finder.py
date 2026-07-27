"""
ComicMetadataHub Candidate Finder

Finds possible comic records from
provider databases.
"""


from src.comicvine.database import (
    get_connection as get_comicvine_connection
)


from src.gcd.database import (
    get_connection as get_gcd_connection
)



class CandidateFinder:
    """
    Finds possible comic matches.
    """



    def find_candidates(
        self,
        record,
        candidates
    ):

        results = []


        for candidate in candidates:

            if (
                candidate.get("title")
                ==
                record.get("title")
                and
                candidate.get("issue_number")
                ==
                record.get("issue")
            ):

                results.append(
                    candidate
                )


        return results



    def search_database(
        self,
        connection,
        table,
        field_or_value,
        value=None
    ):
        """
        Generic database search helper.

        Supports:
            search_database(
                connection,
                table,
                value
            )

        and:

            search_database(
                connection,
                table,
                field,
                value
            )
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

            AND comicvine_issues.issue_number = ?
            """,
            (
                record.get("title"),
                record.get("issue")
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

            AND gcd_issues.issue_number = ?
            """,
            (
                record.get("title"),
                record.get("issue")
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
