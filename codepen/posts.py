"""This module implements the Posts functionality of python-codepen"""
from codepen.base import _CodePen


class Posts(_CodePen):
    """
    Posts functionality.

    See: http://cpv2api.com/#posts
    """

    def list(self, category=None, **kwargs):
        """
        Get a list of blog posts in a specified category.

        Args:
            category: The category of the desired data.
                (Options: 'picks' | 'popular')
                (Default: 'popular')
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of blog posts (dicts) returned from the API.
        """
        category = self._get_category(category)
        path = 'posts/{category}'.format(category=category)

        response = self._request(path, kwargs)
        return response
