"""
ComicMetadataHub Field Rules

Defines field-specific metadata behavior.
"""


class FieldRules:
    """
    Rules for individual metadata fields.
    """

    def __init__(self):

        self.rules = {

            "title": "review",

            "series": "review",

            "issue": "review",

            "publisher": "priority",

            "writer": "conflict",

            "artist": "conflict",

            "summary": "prefer_complete",

            "cover": "prefer_quality"

        }



    def get_rule(
        self,
        field_name
    ):

        return self.rules.get(
            field_name,
            "default"
        )
