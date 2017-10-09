"""
MODULE DOCSTRING: FILL IN LATER
"""
from codepen.base import _CodePen


class Posts(_CodePen):
    """
    CLASS DOCSTRING: FILL IN LATER
    """

    def list(self, category=None, **kwargs):
        """
        Get a list of posts with respect to a category.

        Args:
            category: 'picks' | 'popular'
                (default: 'popular')
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        category = self._get_category(category)
        path = 'posts/{category}'.format(category=category)

        response = self._request(path, kwargs)
        return response
