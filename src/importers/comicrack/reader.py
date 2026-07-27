"""
ComicRack ComicInfo.xml Reader

Reads ComicInfo.xml files and converts
them into dictionaries for the ComicRack mapper.
"""


import xml.etree.ElementTree as ET



class ComicInfoReader:
    """
    Reads ComicInfo.xml metadata.
    """


    def read_file(
        self,
        filename
    ):
        """
        Read ComicInfo.xml from disk.
        """

        tree = ET.parse(
            filename
        )

        root = tree.getroot()

        return self.read_xml(
            root
        )



    def read_xml(
        self,
        root
    ):
        """
        Convert XML element into dictionary.
        """

        result = {}


        for element in root:

            if element.tag == "Pages":

                continue


            if element.text:

                result[element.tag] = (
                    element.text.strip()
                )


        return result