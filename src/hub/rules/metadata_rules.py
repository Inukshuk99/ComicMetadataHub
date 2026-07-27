"""
ComicMetadataHub Metadata Rules

Determines how metadata values
should be handled during merging.
"""


from src.hub.merge.conflict import (
    MetadataConflict
)


from src.hub.rules.provider_priority import (
    ProviderPriority
)


from src.hub.rules.field_rules import (
    FieldRules
)



class MetadataRules:
    """
    Applies metadata comparison rules.
    """


    def __init__(
        self
    ):

        self.priority = ProviderPriority()

        self.fields = FieldRules()



    def compare(
        self,
        field_name,
        existing_value,
        incoming_value,
        source
    ):
        """
        Compare an incoming value
        against existing metadata.
        """

        field_rule = self.fields.get_rule(
            field_name
        )


        # Empty existing value
        if not existing_value:

            return {
                "action": "fill",
                "value": incoming_value,
                "rule": field_rule
            }



        # Same value
        if existing_value == incoming_value:

            return {
                "action": "accept",
                "value": existing_value,
                "rule": field_rule
            }



        # Different values
        conflict = MetadataConflict(
            field_name
        )


        conflict.add_value(
            "Existing",
            existing_value
        )


        conflict.add_value(
            source,
            incoming_value
        )


        return {
            "action": "conflict",
            "conflict": conflict,
            "rule": field_rule,
            "source_priority": self.priority.get_priority(
                source
            )
        }
