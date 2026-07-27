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


        sql = """
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
        """


        values = []


        for record in records:

            values.append(
                (
                    record.get("gcd_id"),
                    record.get("name"),
                    record.get("start_year"),
                    record.get("end_year")
                )
            )


        count = self.insert_records(
            connection,
            sql,
            values
        )


        connection.close()


        return count
