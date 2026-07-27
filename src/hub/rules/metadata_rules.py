"""
ComicMetadataHub Metadata Rules

Determines how metadata values
should be handled during merging.
"""


from src.hub.merge.conflict import (
    MetadataConflict
)



class MetadataRules:
    """
    Applies metadata comparison rules.
    """



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

        # Empty existing value
        if not existing_value:

            return {
                "action": "fill",
                "value": incoming_value
            }



        # Same value
        if existing_value == incoming_value:

            return {
                "action": "accept",
                "value": existing_value
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
            "conflict": conflict
        }
