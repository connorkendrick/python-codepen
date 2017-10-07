import requests

class Pens(object):
    @staticmethod
    def list(category='picks', page=1):
        """
        Get a list of pens with respect to a category.

        Args:
            category: 'picks' | 'popular' | 'recent'
                (default: 'picks')
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/pens/{}'.format(category)
        response = requests.get(path, params = {'page': str(page)})
        return response.json()['data']

    @staticmethod
    def tag(tag, page=1):
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
        path = 'https://cpv2api.com/tag/{}'.format(tag)
        response = requests.get(path, params = {'page': str(page)})
        return response.json()['data']
