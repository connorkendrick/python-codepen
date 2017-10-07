from .base import CodePen

class Collections(CodePen):
    def __init__(self):
        super(Collections, self).__init__()

    def collection_info(self, ID, **kwargs):
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
        path = 'collection/{ID}'.format(ID=ID)

        response = self._GET(path, kwargs)
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

        response = self._GET(path, kwargs)
        return response
