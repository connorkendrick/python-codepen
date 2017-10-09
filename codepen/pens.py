"""This module implements the Pens functionality of python-codepen"""
from codepen.base import _CodePen


class Pens(_CodePen):
    """
    Pens functionality.

    See: http://cpv2api.com/#pens
    """

    def list(self, category=None, **kwargs):
        """
        Get a list of pens in a specified category.

        Args:
            category: The category of the desired data.
                (Options: 'picks' | 'popular' | 'recent')
                (Default: 'popular')
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
        category = self._get_category(category)
        path = 'pens/{category}'.format(category=category)

        response = self._request(path, kwargs)
        return response

    def tag(self, tag, **kwargs):
        """
        Get a list of pens matching a specified tag.

        Args:
            tag: The tag to select pens by. (Required)
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
        path = 'tag/{tag}'.format(tag=tag)

        response = self._request(path, kwargs)
        return response
