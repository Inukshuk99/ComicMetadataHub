"""
ComicMetadataHub ComicVine Updater

Updates localcv.db with ComicVine data.
"""


from src.updaters.base_updater import (
    BaseUpdater
)


from src.updaters.database_updater import (
    DatabaseUpdater
)


from src.comicvine.database import (
    get_connection
)



class ComicVineUpdater(
    BaseUpdater,
    DatabaseUpdater
):

    """
    Updates localcv.db.
    """


    name = "ComicVine Updater"



    def update(
        self,
        records=None
    ):

        if records is None:

            records = []


        connection = get_connection()


        sql = """
            INSERT OR REPLACE INTO comicvine_series
            (
                comicvine_id,
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
                    record.get("comicvine_id"),
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
