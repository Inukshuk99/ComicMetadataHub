"""
ComicMetadataHub Provider Import Pipeline

Runs imported comics against provider databases.
"""


from src.hub.matching.candidate_finder import (
    CandidateFinder
)


from src.hub.matching.match_pipeline import (
    MatchPipeline
)



class ProviderImportPipeline:
    """
    Imports and matches using provider databases.
    """



    def __init__(self):

        self.finder = CandidateFinder()

        self.pipeline = MatchPipeline()



    def process(
        self,
        record
    ):
        """
        Find provider candidates and match.
        """


        candidates = self.finder.find_provider_candidates(
            record
        )


        return self.pipeline.match(
            record,
            candidates
        )
