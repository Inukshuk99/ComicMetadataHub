"""
ComicMetadataHub Match Importer Test
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


from src.hub.importers.match_importer import (
    MatchImporter
)



def test_match_importer():

    print(
        "Testing match importer..."
    )


    importer = MatchImporter()


    results = importer.process(
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
        "Match importer test passed"
    )



if __name__ == "__main__":

    test_match_importer()
