"""
ComicMetadataHub Comic Import Pipeline Test
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


from src.hub.importers.comic_import_pipeline import (
    ComicImportPipeline
)



def test_comic_import_pipeline():

    print(
        "Testing comic import pipeline..."
    )


    pipeline = ComicImportPipeline()


    results = pipeline.process(
        {
            "title": "Batman",
            "issue": "1",
            "publisher": "DC",
            "year": 1940
        },
        [
            {
                "title": "Batman",
                "issue": "1",
                "publisher": "DC",
                "year": 1940
            }
        ]
    )


    assert len(results) == 1

    assert results[0]["match"].matched


    print(
        "Comic import pipeline test passed"
    )



if __name__ == "__main__":

    test_comic_import_pipeline()
