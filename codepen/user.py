import requests

class User(object):
    def __init__(self, username):
        self.username = username

    def profile(self):
        """
        Get the profile data for a user.

        Returns:
            A dict representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/profile/{}'.format(self.username)
        response = requests.get(path)
        return response.json()['data']
        
    def following_list(self, **kwargs):
        """
        Get a list of users the user is following.

        Args:
            page: (optional) Defaults to 1

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/following/{}'.format(self.username)
        response = requests.get(path, params=kwargs)
        return response.json()['data']

    def follower_list(self, **kwargs):
        """
        Get a list of users that follow the user.

        Args:
            page: (optional) Defaults to 1

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/followers/{}'.format(self.username)
        response = requests.get(path, params=kwargs)
        return response.json()['data']

    def user_tags(self):
        """
        Get a list of tags for the user.

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'https://cpv2api.com/tags/{}'.format(self.username)
        response = requests.get(path)
        return response.json()['data']
