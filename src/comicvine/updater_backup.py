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

        cursor = connection.cursor()

        count = 0


        for record in records:


            record_type = record.get(
                "type"
            )


            if record_type == "issue":

                cursor.execute(
                    """
                    INSERT OR REPLACE INTO comicvine_issues
                    (
                        comicvine_id,
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
                        record.get("comicvine_id"),
                        record.get("series_id"),
                        record.get("issue_number"),
                        record.get("title"),
                        record.get("year")
                    )
                )


            elif record_type == "publisher":

                cursor.execute(
                    """
                    INSERT OR REPLACE INTO comicvine_publishers
                    (
                        comicvine_id,
                        name
                    )
                    VALUES
                    (
                        ?,
                        ?
                    )
                    """,
                    (
                        record.get("comicvine_id"),
                        record.get("name")
                    )
                )


            elif record_type == "creator":

                cursor.execute(
                    """
                    INSERT OR REPLACE INTO comicvine_creators
                    (
                        comicvine_id,
                        name
                    )
                    VALUES
                    (
                        ?,
                        ?
                    )
                    """,
                    (
                        record.get("comicvine_id"),
                        record.get("name")
                    )
                )


            else:

                cursor.execute(
                    """
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
                    """,
                    (
                        record.get("comicvine_id"),
                        record.get("name"),
                        record.get("start_year"),
                        record.get("end_year")
                    )
                )


            count += 1


        connection.commit()

        connection.close()


        return count
