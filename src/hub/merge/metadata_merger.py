"""
ComicMetadataHub Metadata Merger

Combines metadata from multiple sources
using metadata rules.
"""


from src.hub.rules.metadata_rules import (
    MetadataRules
)


from src.hub.rules.provider_priority import (
    ProviderPriority
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

        self.priority = ProviderPriority()



    def merge(
        self,
        existing,
        incoming,
        source
    ):
        """
        Merge incoming metadata into
        existing metadata.
        """

        merged = dict(
            existing
        )

        conflicts = []

        decisions = []



        for field, value in incoming.items():

            result = self.rules.compare(
                field,
                existing.get(field),
                value,
                source
            )


            rule = result.get(
                "rule",
                "default"
            )



            if result["action"] == "fill":

                merged[field] = result["value"]

                decisions.append(
                    {
                        "field": field,
                        "action": "fill",
                        "rule": rule
                    }
                )



            elif result["action"] == "accept":

                merged[field] = result["value"]

                decisions.append(
                    {
                        "field": field,
                        "action": "accept",
                        "rule": rule
                    }
                )



            elif result["action"] == "conflict":

                conflict = result["conflict"]

                decision = {
                    "field": field,
                    "action": "conflict",
                    "rule": rule
                }


                if rule == "priority":

                    winner = conflict.suggest_winner(
                        self.priority
                    )


                    decision["suggested_source"] = (
                        winner
                    )


                    if winner:

                        decision["suggested_value"] = (
                            conflict.values[winner]
                        )


                elif rule == "review":

                    decision["requires_review"] = True



                conflicts.append(
                    conflict
                )


                decisions.append(
                    decision
                )



        return {
            "data": merged,
            "conflicts": conflicts,
            "decisions": decisions
        }
