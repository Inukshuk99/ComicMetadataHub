"""
ComicMetadataHub Application Entry Point
"""


from core.logger import logger

from services.metadata_service import (
    MetadataService
)

from importers.comicrack.importer import (
    ComicRackImporter
)



def main():

    logger.info(
        "ComicMetadataHub starting"
    )


    service = MetadataService()


    comicrack = ComicRackImporter()


    service.register_source(
        comicrack
    )


    logger.info(
        "ComicMetadataHub initialized"
    )


    print(
        "ComicMetadataHub startup complete"
    )



if __name__ == "__main__":

    main()
