"""
ComicMetadataHub Candidate Normalizer Provider Test
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


from src.hub.normalization.candidate_normalizer import (
    CandidateNormalizer
)



def test_candidate_normalizer_provider():

    print(
        "Testing provider candidate normalization..."
    )


    normalizer = CandidateNormalizer()


    comicvine = normalizer.normalize(
        {
            "comicvine_id": "105811",
            "title": "Batman",
            "issue_number": "1",
            "year": 1940,
            "source": "ComicVine"
        }
    )


    assert comicvine["issue"] == "1"

    assert comicvine["identifiers"]["comicvine"] == (
        "105811"
    )

    assert comicvine["metadata_provider"] == (
        "ComicVine"
    )



    gcd = normalizer.normalize(
        {
            "gcd_id": "98765",
            "title": "Batman",
            "issue_number": "1",
            "year": 1940,
            "source": "GCD"
        }
    )


    assert gcd["issue"] == "1"

    assert gcd["identifiers"]["gcd"] == (
        "98765"
    )

    assert gcd["metadata_provider"] == (
        "GCD"
    )


    print(
        "Candidate normalizer provider test passed"
    )



if __name__ == "__main__":

    test_candidate_normalizer_provider()
