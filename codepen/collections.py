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

            Keys for pen data:
                [title]: Title of the pen.
                [details]: Details of the pen.
                [link]: Link to the pen.
                [id]: Pen's ID.
                [views]: Number of views.
                [loves]: Number of loves.
                [comments]: Number of comments.
                [images]: Image data for the pen. (dict)
                    Keys for images:
                        [small]: Small image of pen.
                        [large]: Large image of pen.
                [user]: User data for the pen. (dict)
                    Keys for user:
                        [nicename]: The user's actual name.
                        [username]: The user's username.
                        [avatar]: Link to the user's avatar image.
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

            Keys for collection data:
                [title]: Title of the collection.
                [details]: Details of the collection.
                [id]: Collection's ID.
                [url]: Link to the collection.
                [penCount]: Number of pens in collection.
                [loves]: Number of loves.
                [views]: Number of views.
                [user]: User data for the collection. (dict)
                    Keys for user:
                        [nicename]: The user's actual name.
                        [username]: The user's username.
                        [avatar]: Link to the user's avatar image.
                        [profileUrl]: Link to the user's profile.
        """
        category = self._get_category(category)
        path = 'collections/{category}'.format(category=category)

        response = self._request(path, kwargs)
        return response
