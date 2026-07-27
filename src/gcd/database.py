"""
ComicMetadataHub GCD Database

Local cache database for GCD data.
"""

import sqlite3
import os


from src.core.config import (
    GCD_DATABASE_FILE
)



def ensure_database_directory():

    directory = os.path.dirname(
        GCD_DATABASE_FILE
    )

    if not os.path.exists(directory):

        os.makedirs(directory)



def get_connection():

    ensure_database_directory()


    connection = sqlite3.connect(
        GCD_DATABASE_FILE
    )


    connection.row_factory = sqlite3.Row


    return connection



def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gcd_publishers (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            gcd_id TEXT UNIQUE,

            name TEXT

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gcd_series (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            gcd_id TEXT UNIQUE,

            publisher_id INTEGER,

            name TEXT,

            start_year INTEGER,

            end_year INTEGER

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gcd_issues (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            gcd_id TEXT UNIQUE,

            series_id INTEGER,

            issue_number TEXT,

            title TEXT,

            year INTEGER

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gcd_creators (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            gcd_id TEXT UNIQUE,

            name TEXT

        )
    """)



    connection.commit()

    connection.close()
