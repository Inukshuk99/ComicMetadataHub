"""
ComicRack Mapper Test
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


from src.importers.comicrack.mapper import (
    ComicRackMapper
)



def test_comicrack_mapper():

    print(
        "Testing ComicRack mapper..."
    )


    mapper = ComicRackMapper()


    comicinfo = {

        "Title":
            "The Legend of the Batman",

        "Series":
            "Batman",

        "Number":
            "1",

        "Count":
            "1",

        "Volume":
            "1940",

        "Year":
            "1940",

        "Writer":
            "Bill Finger, Paul Gustavson",

        "Artist":
            "Bob Kane",

        "Penciller":
            "Bob Kane, George Papp",

        "Publisher":
            "DC Comics",

        "Characters":
            "Batman, Joker",

        "Teams":
            "Batman and Robin",

        "Locations":
            "Gotham City",

        "Tags":
            "CVDB105811",

        "Notes":
            "Scraped metadata from ComicVine [CVDB105811].",

        "PageCount":
            "54",

        "LanguageISO":
            "en",

        "Format":
            "Series",

    }


    result = mapper.map(
        comicinfo
    )


    assert result["title"] == (
        "The Legend of the Batman"
    )


    assert result["series"] == (
        "Batman"
    )


    assert result["issue"] == (
        "1"
    )


    # Volume year detection

    assert result["volume_year"] == (
        1940
    )


    # Creator splitting

    assert (
        "Bill Finger"
        in
        result["creators"]["writer"]
    )


    assert (
        "Paul Gustavson"
        in
        result["creators"]["writer"]
    )


    # Lists

    assert (
        "Batman"
        in
        result["characters"]
    )


    # ComicVine ID

    assert result["identifiers"]["comicvine"] == (
        "105811"
    )


    print(
        "ComicRack mapper test passed"
    )



if __name__ == "__main__":

    test_comicrack_mapper()