"""
ComicInfo Writer Test
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


from src.exporters.comicrack.writer import (
    ComicInfoWriter
)



def test_comicinfo_writer():

    print(
        "Testing ComicInfo writer..."
    )


    writer = ComicInfoWriter()


    xml = writer.write(
        {
            "title": "Batman",

            "series": "Batman",

            "issue": "1",

            "publisher": "DC",

            "year": 1940,

            "creators": {

                "writer": [
                    "Bill Finger"
                ]

            },

            "characters": [

                "Batman"

            ]

        }
    )


    text = xml.decode(
        "utf-8"
    )


    assert "<Title>Batman</Title>" in text

    assert "<Series>Batman</Series>" in text

    assert "<Number>1</Number>" in text

    assert "<Publisher>DC</Publisher>" in text

    assert "<Writer>Bill Finger</Writer>" in text


    print(
        "ComicInfo writer test passed"
    )



if __name__ == "__main__":

    test_comicinfo_writer()
