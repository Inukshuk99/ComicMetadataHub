"""
ComicMetadataHub Startup Test
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


from src.core.logger import logger
from src.services.metadata_service import MetadataService
from src.importers.comicrack_importer import ComicRackImporter


def test_startup():

    logger.info(
        "Test started"
    )

    service = MetadataService()

    importer = ComicRackImporter()

    service.register_source(
        importer
    )

    assert importer.name == "ComicRack"

    print(
        "ComicMetadataHub startup test passed"
    )


if __name__ == "__main__":
    test_startup()