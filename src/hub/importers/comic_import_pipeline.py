"""
ComicMetadataHub Comic Import Pipeline

Connects comic importers with
metadata matching.
"""


from .match_importer import MatchImporter



class ComicImportPipeline:
    """
    Runs imported comics through matching.
    """



    def __init__(self):

        self.matcher = MatchImporter()



    def process(
        self,
        comic_record,
        candidates
    ):
        """
        Process imported comic metadata.
        """


        return self.matcher.process(
            comic_record,
            candidates
        )
