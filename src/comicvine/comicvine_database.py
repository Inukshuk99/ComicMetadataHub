"""
ComicMetadataHub ComicVine Database

Local cache database for ComicVine data.
"""

import sqlite3
import os


from src.core.config import (
    COMICVINE_DATABASE_FILE
)



def ensure_database_directory():

    directory = os.path.dirname(
        COMICVINE_DATABASE_FILE
    )

    if not os.path.exists(directory):

        os.makedirs(directory)



def get_connection():

    ensure_database_directory()


    connection = sqlite3.connect(
        COMICVINE_DATABASE_FILE
    )


    connection.row_factory = sqlite3.Row


    return connection



def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comicvine_publishers (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            comicvine_id TEXT UNIQUE,

            name TEXT

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comicvine_series (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            comicvine_id TEXT UNIQUE,

            publisher_id INTEGER,

            name TEXT,

            start_year INTEGER,

            end_year INTEGER

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comicvine_issues (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            comicvine_id TEXT UNIQUE,

            series_id INTEGER,

            issue_number TEXT,

            title TEXT,

            year INTEGER

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comicvine_creators (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            comicvine_id TEXT UNIQUE,

            name TEXT

        )
    """)



    connection.commit()

    connection.close()
