"""
ComicMetadataHub Match Importer

Runs imported records through
the matching pipeline.
"""


from src.hub.matching.match_pipeline import (
    MatchPipeline
)



class MatchImporter:
    """
    Adds matching to imported records.
    """



    def __init__(self):

        self.pipeline = MatchPipeline()



    def process(
        self,
        record,
        candidates
    ):
        """
        Match an imported record.
        """


        return self.pipeline.match(
            record,
            candidates
        )
