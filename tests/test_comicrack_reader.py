"""
ComicRack ComicInfo Reader Test
"""


import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from src.importers.comicrack.reader import (
    ComicInfoReader
)



def test_comicrack_reader():

    print(
        "Testing ComicRack XML reader..."
    )


    xml = """
    <ComicInfo>
        <Title>Test Batman</Title>
        <Series>Batman</Series>
        <Number>1</Number>
        <Writer>Bill Finger</Writer>
        <Publisher>DC Comics</Publisher>
    </ComicInfo>
    """


    import xml.etree.ElementTree as ET


    root = ET.fromstring(
        xml
    )


    reader = ComicInfoReader()


    result = reader.read_xml(
        root
    )


    assert result["Title"] == (
        "Test Batman"
    )


    assert result["Series"] == (
        "Batman"
    )


    assert result["Number"] == (
        "1"
    )


    assert result["Writer"] == (
        "Bill Finger"
    )


    assert result["Publisher"] == (
        "DC Comics"
    )


    print(
        "ComicRack XML reader test passed"
    )



if __name__ == "__main__":

    test_comicrack_reader()