"""
ComicMetadataHub Provider Import Pipeline Test
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


from src.hub.importers.provider_import_pipeline import (
    ProviderImportPipeline
)



def test_provider_import_pipeline():

    print(
        "Testing provider import pipeline..."
    )


    pipeline = ProviderImportPipeline()


    results = pipeline.process(
        {
            "title": "Batman",
            "issue": "1",
            "publisher": "DC",
            "year": 1940
        }
    )


    assert isinstance(
        results,
        list
    )


    print(
        "Provider import pipeline test passed"
    )



if __name__ == "__main__":

    test_provider_import_pipeline()
