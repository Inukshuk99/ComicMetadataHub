"""
ComicMetadataHub Database Layer

Handles SQLite database connections and initialization.
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
    Creates ComicMetadataHub database tables.
    """

    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            publisher_type TEXT
        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS titles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id)
                REFERENCES publishers(id)
        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS series (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title_id INTEGER,
            official_name TEXT,
            display_name TEXT,
            volume INTEGER,
            start_year INTEGER,
            end_year INTEGER,
            FOREIGN KEY (title_id)
                REFERENCES titles(id)
        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS issues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            series_id INTEGER,
            number TEXT,
            title TEXT,
            cover_date TEXT,
            release_date TEXT,
            FOREIGN KEY (series_id)
                REFERENCES series(id)
        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS editions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            issue_id INTEGER,
            edition_type TEXT,
            variant_name TEXT,
            printing INTEGER,
            FOREIGN KEY (issue_id)
                REFERENCES issues(id)
        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comic_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            edition_id INTEGER,
            filename TEXT,
            path TEXT,
            format TEXT,
            checksum TEXT,
            FOREIGN KEY (edition_id)
                REFERENCES editions(id)
        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metadata_sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            source_type TEXT,
            confidence REAL
        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metadata_values (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_type TEXT NOT NULL,
            entity_id INTEGER NOT NULL,
            field_name TEXT NOT NULL,
            value TEXT,
            source_id INTEGER,
            confidence REAL,
            FOREIGN KEY (source_id)
                REFERENCES metadata_sources(id)
        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metadata_conflicts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_type TEXT NOT NULL,
            entity_id INTEGER NOT NULL,
            field_name TEXT NOT NULL,
            status TEXT DEFAULT 'Open',
            selected_source TEXT
        )
    """)



    connection.commit()

    connection.close()



    logger.info(
        "Database initialized successfully"
    )
