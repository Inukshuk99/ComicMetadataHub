"""
ComicMetadataHub Metadata Service

Handles normalization and processing of imported metadata.
"""


from ..core.logger import logger


class MetadataService:

    def __init__(self):
        self.sources = []


    def register_source(self, importer):
        """
        Register a metadata importer.
        """

        self.sources.append(importer)

        logger.info(
            "Registered metadata source: %s",
            importer.name
        )


    def normalize_metadata(self, data):
        """
        Normalize imported metadata.

        Future versions will:
        - Merge sources
        - Resolve conflicts
        - Apply confidence scores
        """

        logger.info(
            "Normalizing metadata"
        )

        return data


    def process_import(self, importer, identifier):
        """
        Run an import through the metadata pipeline.
        """

        logger.info(
            "Processing import: %s",
            importer.name
        )

        data = importer.import_metadata(
            identifier
        )

        return self.normalize_metadata(
            data
        )