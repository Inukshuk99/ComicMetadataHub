"""
ComicMetadataHub Match Pipeline

Coordinates candidate discovery,
ranking, and identity resolution.
"""


from .candidate_finder import CandidateFinder

from .candidate_ranker import CandidateRanker

from .identity_resolver import IdentityResolver



class MatchPipeline:
    """
    Complete comic matching workflow.
    """



    def __init__(self):

        self.finder = CandidateFinder()

        self.ranker = CandidateRanker()

        self.resolver = IdentityResolver()



    def match(
        self,
        record,
        candidates
    ):
        """
        Find, rank, and resolve candidates.
        """


        found = self.finder.find_candidates(
            record,
            candidates
        )


        ranked = self.ranker.rank(
            record,
            found
        )


        results = []


        for score, candidate in ranked:

            result = self.resolver.resolve(
                record,
                candidate
            )


            results.append(
                {
                    "candidate": candidate,
                    "rank_score": score,
                    "match": result
                }
            )


        return results
