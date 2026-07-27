"""
ComicMetadataHub Importer Test
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


from src.importers.base_importer import BaseImporter
from src.importers.metadata_result import MetadataResult


class TestImporter(BaseImporter):

    name = "Test Importer"


    def can_import(
        self,
        source
    ):

        return True


    def import_metadata(
        self,
        source
    ):

        return MetadataResult(
            source=self.name,
            data={
                "title": "Batman",
                "issue": "1"
            }
        )


def test_importers():

    print(
        "Testing importer framework..."
    )


    importer = TestImporter()


    assert importer.get_name() == "Test Importer"

    assert importer.can_import(
        "test"
    )


    result = importer.import_metadata(
        "test"
    )


    assert result.success

    assert result.source == "Test Importer"

    assert result.data["title"] == "Batman"


    print(
        "Importer test passed"
    )


if __name__ == "__main__":
    test_importers()