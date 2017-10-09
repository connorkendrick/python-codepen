"""
MODULE DOCSTRING: FILL IN DURING DOCUMENTATION PROCESS
"""
from codepen.base import _CodePen


class Collections(_CodePen):
    """
    CLASS DOCSTRING: FILL IN DURING DOCUMENTATION PROCESS
    """

    def collection_info(self, collection_id, **kwargs):
        """
        Get the info (contents) of a collection.

        Args:
            ID: The ID of the desired collection.
                (required)
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'collection/{collection_id}'.format(collection_id=collection_id)

        response = self._request(path, kwargs)
        return response

    def list(self, category=None, **kwargs):
        """
        Get a list of collections with respect to a category.

        Args:
            category: 'picks' | 'popular'
                (default: 'popular')
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        category = self._get_category(category)
        path = 'collections/{category}'.format(category=category)

        response = self._request(path, kwargs)
        return response
