"""
ComicMetadataHub Database Layer

Handles SQLite database connections.
"""

import sqlite3
import os

from .config import DATABASE_FILE
from .logger import logger


def ensure_database_directory():
    """
    Makes sure the database folder exists.
    """

    directory = os.path.dirname(
        DATABASE_FILE
    )

    if not os.path.exists(directory):
        os.makedirs(directory)


def get_connection():
    """
    Returns a SQLite database connection.
    """

    ensure_database_directory()

    try:
        connection = sqlite3.connect(
            DATABASE_FILE
        )

        connection.row_factory = sqlite3.Row

        return connection

    except Exception as error:
        logger.error(
            "Database connection failed: %s",
            error
        )

        raise


def initialize_database():
    """
    Creates initial database structure.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS metadata_sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            source_type TEXT,
            confidence REAL
        )
        """
    )

    connection.commit()
    connection.close()

    logger.info(
        "Database initialized"
    )