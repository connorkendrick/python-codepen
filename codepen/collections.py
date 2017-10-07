import requests

class Collections(object):
    @staticmethod
    def collection_info(ID, page=1):
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
        path = 'https://cpv2api.com/collection/{}'.format(ID)
        response = requests.get(path, params = {'page': str(page)})
        return response.json()['data']

    @staticmethod
    def list(category='picks', page=1):
        """
        Get a list of collections with respect to a category.

        Args:
            category: 'picks' | 'popular'
                (default: 'picks')
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/collections/{}'.format(category)
        response = requests.get(path, params = {'page': str(page)})
        return response.json()['data']
