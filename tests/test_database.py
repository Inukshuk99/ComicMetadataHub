"""
ComicMetadataHub Database Test
"""

import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from src.core.database import (
    initialize_database,
    get_connection
)

from src.core.config import DATABASE_FILE


def test_database():

    print(
        "Initializing database..."
    )

    initialize_database()


    assert os.path.exists(
        DATABASE_FILE
    )


    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """
    )


    tables = [
        row["name"]
        for row in cursor.fetchall()
    ]


    connection.close()


    required_tables = [
        "publishers",
        "titles",
        "series",
        "issues",
        "editions",
        "comic_files",
        "metadata_sources"
    ]


    for table in required_tables:

        assert table in tables, (
            "Missing database table: "
            + table
        )


    print(
        "Database test passed"
    )


if __name__ == "__main__":
    test_database()