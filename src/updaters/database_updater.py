"""
ComicMetadataHub Database Updater Helper

Common database operations used by
provider updaters.
"""


class DatabaseUpdater:
    """
    Shared database update helper.
    """



    def insert_records(
        self,
        connection,
        sql,
        records
    ):
        """
        Execute insert/update operations.
        """

        cursor = connection.cursor()


        count = 0


        for record in records:

            cursor.execute(
                sql,
                record
            )

            count += 1


        connection.commit()


        return count
