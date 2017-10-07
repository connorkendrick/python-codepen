from .base import CodePen

class Search(CodePen):
    def __init__(self):
        super(Search, self).__init__()

    def pens(self, **kwargs):
        """
        Get a list of pens with respect to a keyword.

        Args:
            q: The query (keyword) searched for.
                (required)
            limit: A username to limit the search by.
                (optional)
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'search/pens'

        response = self._GET(path, kwargs)
        return response

    def posts(self, **kwargs):
        """
        Get a list of posts with respect to a keyword.

        Args:
            q: The query (keyword) searched for.
                (required)
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'search/posts'

        response = self._GET(path, kwargs)
        return response

    def collections(self, **kwargs):
        """
        Get a list of collections with respect to a keyword.

        Args:
            q: The query (keyword) searched for.
                (required)
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'search/collections'

        response = self._GET(path, kwargs)
        return response
