"""
ComicMetadataHub Test Runner
"""

import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from tests.test_startup import test_startup
from tests.test_database import test_database
from tests.test_models import test_models
from tests.test_importers import test_importers
from tests.test_archive_reader import test_archive_reader
from tests.test_comicrack_reader import test_comicrack_reader
from tests.test_comicrack_mapper import test_comicrack_mapper
from tests.test_comicrack_importer import test_comicrack_importer
from tests.test_resolver import test_resolver
from tests.test_comicvine import test_comicvine



def main():

    print(
        "Running startup test..."
    )

    test_startup()


    print(
        "Running database test..."
    )

    test_database()


    print(
        "Running model test..."
    )

    test_models()


    print(
        "Running importer test..."
    )

    test_importers()


    print(
        "Running archive reader test..."
    )

    test_archive_reader()


    print(
        "Running ComicRack reader test..."
    )

    test_comicrack_reader()


    print(
        "Running ComicRack mapper test..."
    )

    test_comicrack_mapper()


    print(
        "Running ComicRack importer test..."
    )

    test_comicrack_importer()


    print(
        "Running resolver test..."
    )

    test_resolver()


    print(
        "Running ComicVine provider test..."
    )

    test_comicvine()


    print(
        "All tests passed."
    )



if __name__ == "__main__":

    main()
