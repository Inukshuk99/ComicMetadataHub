"""
ComicMetadataHub Match Pipeline

Coordinates candidate discovery,
normalization, ranking,
and identity resolution.
"""


from .candidate_finder import CandidateFinder

from .candidate_ranker import CandidateRanker

from .identity_resolver import IdentityResolver

from src.hub.normalization.candidate_normalizer import (
    CandidateNormalizer
)



class MatchPipeline:
    """
    Complete comic matching workflow.
    """



    def __init__(self):

        self.finder = CandidateFinder()

        self.normalizer = CandidateNormalizer()

        self.ranker = CandidateRanker()

        self.resolver = IdentityResolver()



    def match(
        self,
        record,
        candidates
    ):
        """
        Find, normalize, rank,
        and resolve candidates.
        """


        found = self.finder.find_candidates(
            record,
            candidates
        )


        normalized = self.normalizer.normalize_many(
            found
        )


        ranked = self.ranker.rank(
            record,
            normalized
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
