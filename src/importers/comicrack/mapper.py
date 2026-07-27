"""
ComicRack ComicInfo.xml Mapper

Converts ComicInfo.xml metadata into
ComicMetadataHub normalized metadata.
"""


import re


class ComicRackMapper:
    """
    Maps ComicInfo.xml fields into
    standard ComicMetadataHub metadata.
    """


    def map(self, comicinfo):
        """
        Convert ComicInfo.xml dictionary
        into normalized metadata.
        """

        result = {}


        # Basic comic information

        self._copy(
            comicinfo,
            result,
            "Title",
            "title"
        )

        self._copy(
            comicinfo,
            result,
            "Series",
            "series"
        )

        self._copy(
            comicinfo,
            result,
            "Number",
            "issue"
        )

        self._copy(
            comicinfo,
            result,
            "Count",
            "issue_count"
        )


        # Dates

        self._copy(
            comicinfo,
            result,
            "Year",
            "year"
        )

        self._copy(
            comicinfo,
            result,
            "Month",
            "month"
        )

        self._copy(
            comicinfo,
            result,
            "Day",
            "day"
        )


        # Volume handling
        #
        # ComicRack CE may store
        # publication year in Volume.
        #

        if "Volume" in comicinfo:

            volume = comicinfo["Volume"]

            if str(volume).isdigit():

                value = int(volume)

                if 1900 <= value <= 2100:

                    result["volume_year"] = value

                else:

                    result["volume"] = value

            else:

                result["volume"] = volume



        # Publishing

        self._copy(
            comicinfo,
            result,
            "Publisher",
            "publisher"
        )

        self._copy(
            comicinfo,
            result,
            "Imprint",
            "imprint"
        )


        # Creators

        result["creators"] = {}


        creator_fields = {

            "Writer": "writer",

            "Penciller": "penciller",

            "Inker": "inker",

            "Colorist": "colorist",

            "Letterer": "letterer",

            "CoverArtist": "cover_artist",

            "Editor": "editor",

        }


        for source, target in creator_fields.items():

            if source in comicinfo:

                result["creators"][target] = (
                    self._split_list(
                        comicinfo[source]
                    )
                )


        # Classification

        for field in [

            "Genre",
            "Tags",
            "Characters",
            "Teams",
            "Locations",
            "StoryArc",
            "SeriesGroup",
            "MainCharacterOrTeam",

        ]:

            if field in comicinfo:

                result[
                    self._normalize(field)
                ] = self._split_list(
                    comicinfo[field]
                )


        # Description

        self._copy(
            comicinfo,
            result,
            "Summary",
            "summary"
        )

        self._copy(
            comicinfo,
            result,
            "Notes",
            "notes"
        )


        # External information

        self._copy(
            comicinfo,
            result,
            "Web",
            "source_url"
        )


        # Technical information

        self._copy(
            comicinfo,
            result,
            "PageCount",
            "page_count"
        )

        self._copy(
            comicinfo,
            result,
            "LanguageISO",
            "language"
        )

        self._copy(
            comicinfo,
            result,
            "Format",
            "format"
        )

        self._copy(
            comicinfo,
            result,
            "AgeRating",
            "age_rating"
        )


        # ComicVine ID extraction

        identifier = self.extract_comicvine_id(
            comicinfo
        )

        if identifier:

            result["identifiers"] = {

                "comicvine": identifier

            }


        return result



    def extract_comicvine_id(
        self,
        comicinfo
    ):

        """
        Extract ComicVine ID from
        Notes or Tags.
        """

        values = [

            comicinfo.get(
                "Notes",
                ""
            ),

            comicinfo.get(
                "Tags",
                ""
            ),

        ]


        for value in values:

            match = re.search(
                r"CVDB(\d+)",
                str(value)
            )

            if match:

                return match.group(1)


        return None



    def _copy(
        self,
        source,
        target,
        source_key,
        target_key
    ):

        if source_key in source:

            target[target_key] = (
                source[source_key]
            )



    def _split_list(
        self,
        value
    ):

        if not value:

            return []


        return [

            item.strip()

            for item in str(value).split(",")

            if item.strip()

        ]



    def _normalize(
        self,
        value
    ):

        return value.lower()