"""This module implements the Search functionality of python-codepen"""
from codepen.base import _CodePen


class Search(_CodePen):
    """
    Search functionality.

    See: http://cpv2api.com/#search
    """

    def pens(self, **kwargs):
        """
        Get a list of pens with respect to a specified keyword.

        Args:
            q: The keyword to retrieve pens by. (Required)
            limit: A username to limit the search by. (Optional)
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of pens (dicts) returned from the API.
        """
        path = 'search/pens'

        response = self._request(path, kwargs)
        return response

    def posts(self, **kwargs):
        """
        Get a list of blog posts with respect to a specified keyword.

        Args:
            q: The keyword to retrieve blog posts by. (Required)
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of blog posts (dicts) returned from the API.
        """
        path = 'search/posts'

        response = self._request(path, kwargs)
        return response

    def collections(self, **kwargs):
        """
        Get a list of collections with respect to a specified keyword.

        Args:
            q: The keyword to retrieve collections by. (Required)
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of collections (dicts) returned from the API.
        """
        path = 'search/collections'

        response = self._request(path, kwargs)
        return response
