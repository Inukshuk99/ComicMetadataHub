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


        provider = candidate.get(
            "source",
            candidate.get(
                "metadata_provider",
                ""
            )
        )


        issue = candidate.get(
            "issue",
            candidate.get(
                "issue_number"
            )
        )


        title = candidate.get(
            "title"
        )


        if not title:

            title = candidate.get(
                "series"
            )


        return {

            "title": title,

            "series": candidate.get(
                "series",
                title
            ),

            "issue": issue,

            "publisher": candidate.get(
                "publisher"
            ),

            "year": candidate.get(
                "year"
            ),

            "identifiers": identifiers,


            "metadata_provider": provider,


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
