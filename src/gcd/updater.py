"""
ComicMetadataHub GCD Updater

Updates localgcd.db with GCD data.
"""


from src.updaters.base_updater import (
    BaseUpdater
)


from src.updaters.database_updater import (
    DatabaseUpdater
)


from src.gcd.database import (
    get_connection
)



class GCDUpdater(
    BaseUpdater,
    DatabaseUpdater
):

    """
    Updates localgcd.db.
    """


    name = "GCD Updater"



    def update(
        self,
        records=None
    ):

        if records is None:

            records = []


        connection = get_connection()


        count = 0


        cursor = connection.cursor()


        for record in records:


            if record.get("type") == "issue":

                cursor.execute(
                    """
                    INSERT OR REPLACE INTO gcd_issues
                    (
                        gcd_id,
                        series_id,
                        issue_number,
                        title,
                        year
                    )
                    VALUES
                    (
                        ?,
                        ?,
                        ?,
                        ?,
                        ?
                    )
                    """,
                    (
                        record.get("gcd_id"),
                        record.get("series_id"),
                        record.get("issue_number"),
                        record.get("title"),
                        record.get("year")
                    )
                )


            else:

                cursor.execute(
                    """
                    INSERT OR REPLACE INTO gcd_series
                    (
                        gcd_id,
                        name,
                        start_year,
                        end_year
                    )
                    VALUES
                    (
                        ?,
                        ?,
                        ?,
                        ?
                    )
                    """,
                    (
                        record.get("gcd_id"),
                        record.get("name"),
                        record.get("start_year"),
                        record.get("end_year")
                    )
                )


            count += 1


        connection.commit()

        connection.close()


        return count
