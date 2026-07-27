"""
ComicMetadataHub Identity Matching Levels Test
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


from src.hub.matching.identity_resolver import (
    IdentityResolver
)



def test_identity_matching_levels():

    print(
        "Testing identity matching levels..."
    )


    resolver = IdentityResolver()



    # Strong match using identifier

    source = {
        "identifier": "CV-12345",
        "publisher": "DC",
        "title": "Batman",
        "series": "Batman",
        "volume": 1,
        "issue": "1",
        "edition": "Standard"
    }


    candidate = {
        "identifier": "CV-12345",
        "publisher": "DC",
        "title": "Batman",
        "series": "Batman",
        "volume": 1,
        "issue": "1",
        "edition": "Standard"
    }



    result = resolver.resolve(
        source,
        candidate
    )


    assert result.matched

    assert result.score >= 100



    # Title and issue match without identifier

    source2 = {
        "publisher": "DC",
        "title": "Batman",
        "series": "Batman",
        "issue": "1"
    }


    candidate2 = {
        "publisher": "DC",
        "title": "Batman",
        "series": "Batman",
        "issue": "1"
    }



    result2 = resolver.resolve(
        source2,
        candidate2
    )


    assert result2.score > 0



    print(
        "Identity matching levels test passed"
    )



if __name__ == "__main__":

    test_identity_matching_levels()
