"""
ComicMetadataHub Data Models

Core metadata objects.
"""


class Publisher:
    def __init__(self, name="", publisher_type=""):
        self.name = name
        self.publisher_type = publisher_type


class Title:
    def __init__(self, name="", publisher=None):
        self.name = name
        self.publisher = publisher


class Series:
    def __init__(
        self,
        official_name="",
        display_name="",
        volume=None,
        start_year=None,
        end_year=None
    ):
        self.official_name = official_name
        self.display_name = display_name
        self.volume = volume
        self.start_year = start_year
        self.end_year = end_year


class Issue:
    def __init__(
        self,
        number="",
        title="",
        cover_date="",
        release_date=""
    ):
        self.number = number
        self.title = title
        self.cover_date = cover_date
        self.release_date = release_date


class Edition:
    def __init__(
        self,
        edition_type="Regular",
        variant_name="",
        printing=1
    ):
        self.edition_type = edition_type
        self.variant_name = variant_name
        self.printing = printing


class ComicFile:
    def __init__(
        self,
        filename="",
        path="",
        file_format="",
        checksum=""
    ):
        self.filename = filename
        self.path = path
        self.file_format = file_format
        self.checksum = checksum


class Creator:
    def __init__(
        self,
        name="",
        role=""
    ):
        self.name = name
        self.role = role


class MetadataSource:
    def __init__(
        self,
        name="",
        confidence=0.0
    ):
        self.name = name
        self.confidence = confidence