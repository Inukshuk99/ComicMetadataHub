"""
ComicMetadataHub Application Entry Point
"""

from core.logger import logger
from core.database import initialize_database

from importers.comicrack_importer import ComicRackImporter
from services.metadata_service import MetadataService


def main():

    logger.info(
        "ComicMetadataHub starting"
    )


    # Initialize database
    initialize_database()


    # Create metadata service
    service = MetadataService()


    # Register import sources
    comicrack = ComicRackImporter()

    service.register_source(
        comicrack
    )


    comicrack.connect()


    logger.info(
        "ComicMetadataHub initialized successfully"
    )


    print(
        "ComicMetadataHub startup complete"
    )


if __name__ == "__main__":
    main()