"""
ComicMetadataHub ComicVine API Client
"""

import os
import json
import urllib.request
import urllib.parse



class ComicVineClient:
    """
    Client for ComicVine API communication.
    """


    BASE_URL = (
        "https://comicvine.gamespot.com/api"
    )


    def __init__(
        self
    ):

        self.api_key = os.environ.get(
            "COMICVINE_API_KEY"
        )



    def is_configured(
        self
    ):

        return bool(
            self.api_key
        )



    def request(
        self,
        endpoint,
        params=None
    ):

        if not self.api_key:

            raise RuntimeError(
                "COMICVINE_API_KEY is not configured"
            )


        if params is None:

            params = {}


        params.update(
            {
                "api_key": self.api_key,
                "format": "json"
            }
        )


        query = urllib.parse.urlencode(
            params
        )


        url = (
            self.BASE_URL
            + endpoint
            + "?"
            + query
        )


        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "ComicMetadataHub"
            }
        )


        with urllib.request.urlopen(
            request,
            timeout=30
        ) as response:

            return json.loads(
                response.read()
            )



    def search(
        self,
        query,
        resource
    ):
        """
        Search ComicVine resources.
        """

        return self.request(
            "/search/",
            {
                "query": query,
                "resources": resource
            }
        )



    def get_volume(
        self,
        volume_id
    ):
        """
        Retrieve a ComicVine volume.
        """

        return self.request(
            "/volume/4025-" + str(volume_id) + "/"
        )



    def get_issue(
        self,
        issue_id
    ):
        """
        Retrieve a ComicVine issue.
        """

        return self.request(
            "/issue/4000-" + str(issue_id) + "/"
        )
