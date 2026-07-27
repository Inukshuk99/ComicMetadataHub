"""
ComicMetadataHub Metadata Merger

Combines metadata from multiple sources
using metadata rules.
"""


from src.hub.rules.metadata_rules import (
    MetadataRules
)



class MetadataMerger:
    """
    Coordinates metadata comparison
    and merging.
    """


    def __init__(
        self
    ):

        self.rules = MetadataRules()



    def merge(
        self,
        existing,
        incoming,
        source
    ):
        """
        Merge incoming metadata into
        existing metadata.

        Returns:
            merged data
            conflicts
        """

        merged = dict(
            existing
        )

        conflicts = []


        for field, value in incoming.items():

            result = self.rules.compare(
                field,
                existing.get(field),
                value,
                source
            )


            if result["action"] == "fill":

                merged[field] = (
                    result["value"]
                )


            elif result["action"] == "accept":

                merged[field] = (
                    result["value"]
                )


            elif result["action"] == "conflict":

                conflicts.append(
                    result["conflict"]
                )


        return {
            "data": merged,
            "conflicts": conflicts
        }
