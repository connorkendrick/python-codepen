import requests

class User(object):
    def __init__(self, username):
        self.username = username

    def profile(self):
        """
        Get the profile data for the user.

        Returns:
            A dict representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/profile/{}'.format(self.username)
        response = requests.get(path)
        return response.json()['data']
        
    def following_list(self, page=1):
        """
        Get a list of users the user is following.

        Args:
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/following/{}'.format(self.username)
        response = requests.get(path, params = {'page': str(page)})
        return response.json()['data']

    def follower_list(self, page=1):
        """
        Get a list of users that follow the user.

        Args:
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/followers/{}'.format(self.username)
        response = requests.get(path, params = {'page': str(page)})
        return response.json()['data']

    def user_tags(self, page=1):
        """
        Get a list of tags for the user.

        Args:
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/tags/{}'.format(self.username)
        response = requests.get(path, params = {'page': str(page)})
        return response.json()['data']

    def pens(self, category='public', tag=None, page=1):
        """
        Get a list of pens by the user.

        Args:
            category: 'public' | 'popular' | 'loved' | 'forked' | 'showcase'
                (default: 'public')
            tag: The tag of the desired data.
                (optional)
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/pens/{}/{}'.format(category, self.username)
        response = requests.get(path, params = {'tag': str(tag), 'page': str(page)})
        return response.json()['data']

    def posts(self, category='published', page=1):
        """
        Get a list of posts by the user.

        Args:
            category: 'published' | 'popular' | 'loved'
                (default: 'published')
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/posts/{}/{}'.format(category, self.username)
        response = requests.get(path, params = {'page': str(page)})
        return response.json()['data']

    def collections(self, category='public', page=1):
        """
        Get a list of collections by the user.

        Args:
            category: 'public' | 'popular' | 'loved'
                (default: 'public')
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/collections/{}/{}'.format(category, self.username)
        response = requests.get(path, params = {'page': str(page)})
        return response.json()['data']
