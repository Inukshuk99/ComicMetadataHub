"""
Comic Archive Reader

Supports standard comic archive containers:

.cbz  - ZIP
.zip  - ZIP
.cbr  - RAR placeholder

Extracts ComicInfo.xml only.
"""


import zipfile
import os



class ComicArchiveReader:
    """
    Reads ComicInfo.xml from comic archives.
    """



    def read(
        self,
        filename
    ):
        """
        Read ComicInfo.xml from archive.
        """

        extension = (
            os.path.splitext(filename)[1]
            .lower()
        )


        if extension in (
            ".cbz",
            ".zip",
        ):

            return self._read_zip(
                filename
            )


        if extension == ".cbr":

            return self._read_rar(
                filename
            )


        raise ValueError(
            "Unsupported comic archive format: "
            + extension
        )



    def _read_zip(
        self,
        filename
    ):
        """
        Read ComicInfo.xml from ZIP archive.
        """

        with zipfile.ZipFile(
            filename,
            "r"
        ) as archive:


            for name in archive.namelist():

                if name.lower().endswith(
                    "comicinfo.xml"
                ):

                    return archive.read(
                        name
                    )


        raise FileNotFoundError(
            "ComicInfo.xml not found"
        )



    def _read_rar(
        self,
        filename
    ):
        """
        Placeholder for CBR support.

        RAR backend will be added separately.
        """

        raise NotImplementedError(
            "CBR/RAR support is not installed yet"
        )