"""
ComicMetadataHub Candidate Ranker

Ranks possible comic matches.
"""


class CandidateRanker:
    """
    Scores and ranks candidates.
    """



    def score(
        self,
        source,
        candidate
    ):
        """
        Calculate candidate confidence score.
        """

        score = 0


        #
        # Strong identity signals
        #

        if (
            source.get("identifier")
            and
            source.get("identifier")
            ==
            candidate.get("identifier")
        ):

            score += 100



        #
        # Title / series
        #

        if (
            source.get("title")
            and
            source.get("title")
            ==
            candidate.get("title")
        ):

            score += 40



        if (
            source.get("series")
            and
            source.get("series")
            ==
            candidate.get("series")
        ):

            score += 40



        #
        # Issue identity
        #

        if (
            source.get("issue")
            and
            source.get("issue")
            ==
            candidate.get("issue")
        ):

            score += 40



        #
        # Volume and edition
        #

        if (
            source.get("volume")
            and
            source.get("volume")
            ==
            candidate.get("volume")
        ):

            score += 20



        if (
            source.get("edition")
            and
            source.get("edition")
            ==
            candidate.get("edition")
        ):

            score += 10



        #
        # Publisher
        #

        if (
            source.get("publisher")
            and
            source.get("publisher")
            ==
            candidate.get("publisher")
        ):

            score += 15



        #
        # Release year
        #

        if (
            source.get("year")
            and
            source.get("year")
            ==
            candidate.get("year")
        ):

            score += 10



        return score



    def rank(
        self,
        source,
        candidates
    ):
        """
        Return candidates sorted by score.
        """


        ranked = []


        for candidate in candidates:

            ranked.append(
                (
                    self.score(
                        source,
                        candidate
                    ),
                    candidate
                )
            )


        ranked.sort(
            key=lambda item: item[0],
            reverse=True
        )


        return ranked
