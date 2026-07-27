"""
ComicMetadataHub Enumerations

Controlled values used throughout the metadata model.
"""

from enum import Enum


class ComicFormat(Enum):
    """
    Physical or digital comic format.
    """

    SINGLE_ISSUE = "Single Issue"
    TRADE_PAPERBACK = "Trade Paperback"
    HARDCOVER = "Hardcover"
    OMNIBUS = "Omnibus"
    ABSOLUTE = "Absolute Edition"
    DIGITAL = "Digital"
    MAGAZINE = "Magazine"
    OTHER = "Other"


class EditionType(Enum):
    """
    Identifies different editions of the same comic.
    """

    STANDARD = "Standard"
    VARIANT = "Variant"
    DIRECT = "Direct Edition"
    NEWSSTAND = "Newsstand"
    REPRINT = "Reprint"
    DELUXE = "Deluxe"
    COLLECTOR = "Collector"


class IdentifierType(Enum):
    """
    External identifiers from metadata sources.
    """

    COMIC_VINE = "Comic Vine"
    GCD = "Grand Comics Database"
    LEAGUE_OF_COMIC_GEEKS = "League of Comic Geeks"
    COMIC_TAGGER = "ComicTagger"
    COMIC_RACK = "ComicRack"

    ISBN = "ISBN"
    UPC = "UPC"
    DIAMOND_CODE = "Diamond Code"

    LOCAL = "Local"


class SourceType(Enum):
    """
    Metadata providers.
    """

    COMIC_RACK = "ComicRack"
    COMIC_TAGGER = "ComicTagger"
    COMIC_VINE = "Comic Vine"
    GCD = "Grand Comics Database"
    LEAGUE_OF_COMIC_GEEKS = "League of Comic Geeks"
    MY_COMIC_LIST = "MyComicList"
    INDYPLANET = "IndyPlanet"

    USER = "User"
