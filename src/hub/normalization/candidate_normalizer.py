"""
ComicMetadataHub Candidate Normalizer

Converts provider candidate records
into the internal matching format.
"""


class CandidateNormalizer:
    """
    Normalizes external candidates.
    """



    def normalize(
        self,
        candidate
    ):
        """
        Convert provider fields into
        ComicMetadataHub matching fields.
        """

        return {

            "title": candidate.get(
                "title"
            ),

            "series": candidate.get(
                "series",
                candidate.get(
                    "title"
                )
            ),

            "issue": candidate.get(
                "issue",
                candidate.get(
                    "issue_number"
                )
            ),

            "publisher": candidate.get(
                "publisher"
            ),

            "year": candidate.get(
                "year"
            ),

            "identifier": candidate.get(
                "identifier",
                candidate.get(
                    "comicvine_id",
                    candidate.get(
                        "gcd_id"
                    )
                )
            ),

            "source": candidate.get(
                "source"
            ),

            "original": candidate

        }



    def normalize_many(
        self,
        candidates
    ):
        """
        Normalize multiple candidates.
        """

        return [
            self.normalize(candidate)
            for candidate in candidates
        ]
