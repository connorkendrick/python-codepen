from .base import CodePen

class Pens(CodePen):
    def __init__(self):
        super(Pens, self).__init__()

    def list(self, category=None, **kwargs):
        """
        Get a list of pens with respect to a category.

        Args:
            category: 'picks' | 'popular' | 'recent'
                (default: 'popular')
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        category = self._get_category(category)
        path = 'pens/{category}'.format(category=category)

        response = self._GET(path, kwargs)
        return response

    def tag(self, tag, **kwargs):
        """
        Get a list of pens with a certain tag.

        Args:
            tag: The tag to select pens by.
                (required)
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'tag/{tag}'.format(tag=tag)

        response = self._GET(path, kwargs)
        return response
