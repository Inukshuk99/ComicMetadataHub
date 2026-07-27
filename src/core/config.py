"""
ComicMetadataHub Configuration

Central location for application settings.
"""

import os


APP_NAME = "ComicMetadataHub"


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)


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


DATABASE_FILE = os.path.join(
    DATABASE_DIR,
    "ComicMetadataHub.db"
)


COMICVINE_DATABASE_FILE = os.path.join(
    DATABASE_DIR,
    "localcv.db"
)


GCD_DATABASE_FILE = os.path.join(
    DATABASE_DIR,
    "localgcd.db"
)
