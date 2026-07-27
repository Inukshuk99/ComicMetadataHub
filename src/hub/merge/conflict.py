"""
ComicMetadataHub Metadata Conflict Model

Represents metadata differences between sources.
"""


from dataclasses import dataclass, field

from typing import Dict, Any



@dataclass
class MetadataConflict:
    """
    Represents a conflict between metadata sources.
    """


    field_name: str


    values: Dict[str, Any] = field(
        default_factory=dict
    )


    selected_source: str = ""


    resolved: bool = False



    def add_value(
        self,
        source: str,
        value: Any
    ):
        """
        Add a source value.
        """

        self.values[source] = value



    def resolve(
        self,
        source: str
    ):
        """
        Select the winning source.
        """

        if source in self.values:

            self.selected_source = source

            self.resolved = True



    def suggest_winner(
        self,
        priority
    ):
        """
        Suggest highest priority source.
        """

        winner = None

        highest = -1


        for source in self.values:

            value = priority.get_priority(
                source
            )

            if value > highest:

                highest = value

                winner = source


        return winner
