"""
ComicMetadataHub Resolver Test
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


from src.resolver.metadata_resolver import (
    MetadataResolver,
)


def test_resolver():

    print(
        "Testing metadata resolver..."
    )


    resolver = MetadataResolver()


    incoming = {
        "title": "Batman",
        "issue": "1",
        "identifier": "4050-12345"
    }


    existing = {
        "title": "Batman",
        "issue": "1",
        "identifier": "4050-12345"
    }


    result = resolver.resolve(
        incoming,
        existing
    )


    assert result.matched

    assert result.score >= 100

    assert "Identifier match" in result.reason


    print(
        "Resolver test passed"
    )


if __name__ == "__main__":
    test_resolver()