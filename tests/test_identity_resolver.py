"""
ComicMetadataHub Identity Resolver Test
"""


import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from src.hub.matching.identity_resolver import (
    IdentityResolver
)



def test_identity_resolver():

    print(
        "Testing identity resolver..."
    )


    resolver = IdentityResolver()


    source = {

        "title": "Batman",

        "issue": "1",

        "identifiers": {

            "comicvine": "CV-12345"

        }

    }


    candidate = {

        "title": "Batman",

        "issue": "1",

        "identifiers": {

            "comicvine": "CV-12345",

            "gcd": "GCD-98765"

        }

    }


    result = resolver.resolve(
        source,
        candidate
    )


    assert result.matched

    assert result.score >= 100


    assert (
        "Comicvine identifier match"
        in result.reasons
    )


    print(
        "Identity resolver test passed"
    )



if __name__ == "__main__":

    test_identity_resolver()
