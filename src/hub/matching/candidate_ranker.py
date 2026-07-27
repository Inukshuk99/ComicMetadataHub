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

        score = 0


        if (
            source.get("title")
            ==
            candidate.get("title")
        ):

            score += 40



        if (
            source.get("issue")
            ==
            candidate.get("issue")
        ):

            score += 40



        if (
            source.get("publisher")
            ==
            candidate.get("publisher")
        ):

            score += 20



        if (
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
