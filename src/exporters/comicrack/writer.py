"""
ComicRack ComicInfo.xml Writer

Converts ComicMetadataHub normalized metadata
into ComicInfo.xml format.
"""


import xml.etree.ElementTree as ET



class ComicInfoWriter:
    """
    Writes normalized metadata as ComicInfo.xml.
    """



    def write(
        self,
        metadata
    ):
        """
        Convert metadata dictionary
        into XML bytes.
        """


        root = ET.Element(
            "ComicInfo"
        )


        fields = {

            "title": "Title",

            "series": "Series",

            "issue": "Number",

            "issue_count": "Count",

            "year": "Year",

            "month": "Month",

            "day": "Day",

            "publisher": "Publisher",

            "imprint": "Imprint",

            "summary": "Summary",

            "notes": "Notes",

            "source_url": "Web",

            "page_count": "PageCount",

            "language": "LanguageISO",

            "format": "Format",

            "age_rating": "AgeRating",

        }


        for source, target in fields.items():

            if source in metadata:

                element = ET.SubElement(
                    root,
                    target
                )

                element.text = str(
                    metadata[source]
                )


        creators = metadata.get(
            "creators",
            {}
        )


        creator_fields = {

            "writer": "Writer",

            "penciller": "Penciller",

            "inker": "Inker",

            "colorist": "Colorist",

            "letterer": "Letterer",

            "cover_artist": "CoverArtist",

            "editor": "Editor",

        }


        for source, target in creator_fields.items():

            if source in creators:

                element = ET.SubElement(
                    root,
                    target
                )

                element.text = ", ".join(
                    creators[source]
                )


        list_fields = {

            "genre": "Genre",

            "tags": "Tags",

            "characters": "Characters",

            "teams": "Teams",

            "locations": "Locations",

            "storyarc": "StoryArc",

        }


        for source, target in list_fields.items():

            if source in metadata:

                element = ET.SubElement(
                    root,
                    target
                )

                element.text = ", ".join(
                    metadata[source]
                )


        return ET.tostring(
            root,
            encoding="utf-8",
            xml_declaration=True
        )
