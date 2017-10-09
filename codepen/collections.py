"""This module implements the Collections functionality of python-codepen"""
from codepen.base import _CodePen


class Collections(_CodePen):
    """
    Collections functionality.

    See: http://cpv2api.com/#collections
    """

    def collection_info(self, collection_id, **kwargs):
        """
        Get the info (contents) of a collection.

        Args:
            collection_id: The id of the desired collection. (Required)
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of pens (dicts) returned from the API.
        """
        path = 'collection/{collection_id}'.format(collection_id=collection_id)

        response = self._request(path, kwargs)
        return response

    def list(self, category=None, **kwargs):
        """
        Get a list of collections in a specified category.

        Args:
            category: The category of the desired data.
                (Options: 'picks' | 'popular')
                (Default: 'popular')
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of collections (dicts) returned from the API.
        """
        category = self._get_category(category)
        path = 'collections/{category}'.format(category=category)

        response = self._request(path, kwargs)
        return response
