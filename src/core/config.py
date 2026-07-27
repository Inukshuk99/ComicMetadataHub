"""
ComicMetadataHub Configuration

Central location for application settings.
"""

import os


APP_NAME = "ComicMetadataHub"


# Project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


# Portable application data directory
DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)


# Data folders
DATABASE_DIR = os.path.join(
    DATA_DIR,
    "Database"
)

METADATA_DIR = os.path.join(
    DATA_DIR,
    "Metadata"
)

COVERS_DIR = os.path.join(
    DATA_DIR,
    "Covers"
)

CACHE_DIR = os.path.join(
    DATA_DIR,
    "Cache"
)

IMPORT_DIR = os.path.join(
    DATA_DIR,
    "Imports"
)

EXPORT_DIR = os.path.join(
    DATA_DIR,
    "Exports"
)

LOG_DIR = os.path.join(
    DATA_DIR,
    "Logs"
)


# Database file
DATABASE_FILE = os.path.join(
    DATABASE_DIR,
    "ComicMetadataHub.db"
)