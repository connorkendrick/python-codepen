import requests

class Posts(object):
    @staticmethod
    def list(category='picks', page=1):
        """
        Get a list of posts with respect to a category.

        Args:
            category: 'picks' | 'popular'
                (default: 'picks')
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/posts/{}'.format(category)
        response = requests.get(path, params = {'page': str(page)})
        return response.json()['data']
