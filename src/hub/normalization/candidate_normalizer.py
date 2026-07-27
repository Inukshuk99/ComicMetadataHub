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


        identifiers = {}


        if candidate.get("comicvine_id"):

            identifiers["comicvine"] = (
                candidate.get("comicvine_id")
            )


        if candidate.get("gcd_id"):

            identifiers["gcd"] = (
                candidate.get("gcd_id")
            )


        if candidate.get("identifier"):

            identifiers["unknown"] = (
                candidate.get("identifier")
            )


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


            "identifiers": identifiers,


            "metadata_provider": candidate.get(
                "metadata_provider",
                candidate.get(
                    "source"
                )
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
