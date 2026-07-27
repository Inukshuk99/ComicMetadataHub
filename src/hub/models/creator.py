"""
ComicMetadataHub Creator Model

Stores creators and their roles.
"""

from dataclasses import dataclass, field

from typing import List


@dataclass
class CreatorRole:
    """
    A creator's role on a comic.
    """

    role: str


@dataclass
class Creator:
    """
    Represents a person involved in comic creation.
    """

    name: str

    first_name: str = ""

    last_name: str = ""

    roles: List[CreatorRole] = field(
        default_factory=list
    )


    def add_role(
        self,
        role: str
    ):
        """
        Add a role if it does not already exist.
        """

        for existing in self.roles:

            if existing.role == role:
                return


        self.roles.append(
            CreatorRole(role)
        )


    def display_name(self):
        """
        Returns preferred display name.
        """

        if self.name:
            return self.name

        return (
            f"{self.first_name} "
            f"{self.last_name}"
        ).strip()
