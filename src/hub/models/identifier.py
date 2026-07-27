"""
ComicMetadataHub Identifier Model

Stores external and internal identifiers
used to match metadata between sources.
"""

from dataclasses import dataclass

from .enums import IdentifierType


@dataclass
class Identifier:
    """
    Represents an identifier from a metadata source.
    """

    identifier_type: IdentifierType
    value: str
    source: str = ""

    def __str__(self):
        if self.source:
            return (
                f"{self.identifier_type.value}: "
                f"{self.value} ({self.source})"
            )

        return (
            f"{self.identifier_type.value}: "
            f"{self.value}"
        )
