from .base import CodePen

class Posts(CodePen):
    def __init__(self):
        super(Posts, self).__init__()

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

        response = self._GET(path, kwargs)
        return response
