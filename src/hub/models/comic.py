"""
ComicMetadataHub Comic Models

Core metadata entities for comics.
"""

from dataclasses import dataclass, field

from typing import List, Optional

from .creator import Creator

from .identifier import Identifier


@dataclass
class Publisher:
    """
    Comic publisher.
    """

    name: str


@dataclass
class Series:
    """
    A comic series.

    Example:
        Batman
        Detective Comics
    """

    name: str

    publisher: Optional[Publisher] = None

    volumes: List["Volume"] = field(
        default_factory=list
    )


@dataclass
class Volume:
    """
    A publishing run/version.

    Example:
        Batman Volume 1
        Batman Volume 2 (New 52)
    """

    name: str

    start_year: Optional[int] = None

    end_year: Optional[int] = None

    issues: List["Issue"] = field(
        default_factory=list
    )


@dataclass
class Issue:
    """
    A single comic issue.

    Example:
        Batman #1
    """

    number: str

    title: str = ""

    year: Optional[int] = None

    creators: List[Creator] = field(
        default_factory=list
    )

    editions: List["Edition"] = field(
        default_factory=list
    )

    identifiers: List[Identifier] = field(
        default_factory=list
    )


@dataclass
class Edition:
    """
    A specific release of an issue.

    Example:
        Standard Cover
        Variant Cover
        Digital
    """

    name: str

    edition_type: str = "Standard"

    files: List["ComicFile"] = field(
        default_factory=list
    )


@dataclass
class ComicFile:
    """
    Physical file information.

    Example:
        Batman_001.cbz
    """

    filename: str

    path: str = ""

    checksum: str = ""
