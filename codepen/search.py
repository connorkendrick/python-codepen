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

            Keys for post data:
                [title]: Title of the post.
                [content]: Content of the post.
                [link]: Link to the post.
                [views]: Number of views.
                [loves]: Number of loves.
                [comments]: Number of comments.
                [user]: User data for the post. (dict)
                    Keys for user:
                        [nicename]: The user's actual name.
                        [username]: The user's username.
                        [avatar]: Link to the user's avatar image.
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
        path = 'search/collections'

        response = self._request(path, kwargs)
        return response
