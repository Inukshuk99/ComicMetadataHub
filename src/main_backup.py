"""
ComicMetadataHub Application Entry Point
"""

from core.logger import logger
from importers.comicrack_importer import ComicRackImporter
from services.metadata_service import MetadataService


def main():

    logger.info(
        "ComicMetadataHub starting"
    )

    service = MetadataService()

    comicrack = ComicRackImporter()

    service.register_source(
        comicrack
    )

    comicrack.connect()

    logger.info(
        "ComicMetadataHub initialized"
    )


if __name__ == "__main__":
    main()