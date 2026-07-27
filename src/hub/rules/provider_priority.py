"""
ComicMetadataHub Provider Priority

Defines preferred metadata sources.
"""


class ProviderPriority:
    """
    Provider ordering rules.
    """

    def __init__(self):

        self.priority = {

            "User": 100,

            "ComicRack": 90,

            "ComicTagger": 80,

            "ComicVine": 70,

            "GCD": 70

        }


    def get_priority(
        self,
        source
    ):

        return self.priority.get(
            source,
            0
        )
