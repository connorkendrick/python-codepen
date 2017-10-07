import requests

class Search(object):
    @staticmethod
    def pens(query, limit, page=1):
        """
        Get a list of pens with respect to a keyword.

        Args:
            query: The keyword searched for.
                (required)
            limit: A username to limit the search by.
                (optional)
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/search/pens'
        response = requests.get(path, params = {'q': str(query), 'limit': str(limit), 'page': str(page)})
        return response.json()['data']

    @staticmethod
    def posts(query, page=1):
        """
        Get a list of posts with respect to a keyword.

        Args:
            query: The keyword searched for.
                (required)
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/search/posts'
        response = requests.get(path, params = {'q': str(query), 'page': str(page)})
        return response.json()['data']

    @staticmethod
    def collections(query, page=1):
        """
        Get a list of collections with respect to a keyword.

        Args:
            query: The keyword searched for.
                (required)
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/search/collections'
        response = requests.get(path, params = {'q': str(query), 'page': str(page)})
        return response.json()['data']
