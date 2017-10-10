"""This module implements the base class of python-codepen."""
import requests


class _CodePen(object):
    # A base class that handles mainly URL-based tasks.

    def __init__(self):
        # Instantiate the API url (and other project-wide variables).
        self.__base_uri = 'https://cpv2api.com'
        self._default_category = 'popular'

    def __get_complete_url(self, path):
        # Connect and return a request-specific path to the API url.
        return '{base_uri}/{path}'.format(base_uri=self.__base_uri, path=path)

    def _get_category(self, category):
        # Return the default category if one is not already assigned.
        if category is None:
            category = self._default_category
        return category

    def _request(self, path, params=None):
        # Request data from the API with a constructed path.
        url = self.__get_complete_url(path)

        if params is None:
            params = {}

        # Convert query values to strings so Requests can parse
        for key in params:
            params[key] = str(params[key])

        response = requests.get(url, params=params)
        return response.json()['data']
