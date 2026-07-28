"""
Comic Archive Writer

Writes ComicInfo.xml into
CBZ and ZIP comic archives.
"""


import zipfile
import os
import tempfile



class ComicArchiveWriter:
    """
    Writes ComicInfo.xml into archives.
    """



    def write(
        self,
        filename,
        xml_data
    ):
        """
        Add or replace ComicInfo.xml.
        """


        extension = (
            os.path.splitext(filename)[1]
            .lower()
        )


        if extension not in (
            ".cbz",
            ".zip",
        ):

            raise ValueError(
                "Unsupported comic format"
            )


        temp = tempfile.NamedTemporaryFile(
            delete=False
        )

        temp.close()


        with zipfile.ZipFile(
            filename,
            "r"
        ) as source, zipfile.ZipFile(
            temp.name,
            "w"
        ) as target:


            for item in source.infolist():

                if item.filename.lower().endswith(
                    "comicinfo.xml"
                ):

                    continue


                target.writestr(
                    item,
                    source.read(
                        item.filename
                    )
                )


            target.writestr(
                "ComicInfo.xml",
                xml_data
            )


        os.replace(
            temp.name,
            filename
        )


        return filename
