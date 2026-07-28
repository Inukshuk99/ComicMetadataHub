"""
ComicMetadataHub Match Pipeline

Coordinates candidate discovery,
normalization, ranking,
identity resolution,
and metadata merging.
"""


from .candidate_finder import CandidateFinder

from .candidate_ranker import CandidateRanker

from .identity_resolver import IdentityResolver

from src.hub.normalization.candidate_normalizer import (
    CandidateNormalizer
)

from src.hub.merge.metadata_merger import (
    MetadataMerger
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

        self.merger = MetadataMerger()



    def match(
        self,
        record,
        candidates
    ):
        """
        Find, normalize, rank,
        resolve, and merge candidates.
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


            merged = None


            if result.decision == "AUTO_APPLY":

                merged = self.merger.merge(
                    record,
                    candidate,
                    candidate.get(
                        "metadata_provider",
                        "Unknown"
                    )
                )


            results.append(
                {
                    "candidate": candidate,
                    "rank_score": score,
                    "match": result,
                    "merged": merged
                }
            )


        return results
