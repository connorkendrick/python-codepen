"""This module implements the User functionality of python-codepen"""
from codepen.base import _CodePen


class User(_CodePen):
    """
    User functionality.

    See: http://cpv2api.com/#profiles
    """

    def __init__(self, username):
        """Instantiate a username variable for the User object."""
        super(User, self).__init__()
        self.username = username

    def profile(self):
        """
        Get the profile data for the user.

        Returns:
            A dict containing the user profile information returned from the API.
        """
        path = 'profile/{username}'.format(username=self.username)

        response = self._request(path)
        return response

    def following_list(self, **kwargs):
        """
        Get a list of users the user is following.

        Args:
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of user profiles (dicts) returned from the API.
        """
        path = 'following/{username}'.format(username=self.username)

        response = self._request(path, kwargs)
        return response

    def follower_list(self, **kwargs):
        """
        Get a list of users that follow the user.

        Args:
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of user profiles (dicts) returned from the API.
        """
        path = 'followers/{username}'.format(username=self.username)

        response = self._request(path, kwargs)
        return response

    def user_tags(self, **kwargs):
        """
        Get a list of tags the user has used.

        Args:
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of tag data (dicts) returned from the API.
        """
        path = 'tags/{username}'.format(username=self.username)

        response = self._request(path, kwargs)
        return response

    def pens(self, category=None, **kwargs):
        """
        Get a list of pens by the user.

        Args:
            category: The category of the desired data.
                (Options: 'public' | 'popular' | 'loved' | 'forked' | 'showcase')
                (Default: 'popular')
            tag: The tag of the desired data. (Optional)
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of pens (dicts) returned from the API.
        """
        category = self._get_category(category)
        path = 'pens/{category}/{username}'.format(category=category, username=self.username)

        response = self._request(path, kwargs)
        return response

    def posts(self, category=None, **kwargs):
        """
        Get a list of blog posts by the user.

        Args:
            category: The category of the desired data.
                (Options: 'published' | 'popular' | 'loved')
                (Default: 'popular')
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of blog posts (dicts) returned from the API.
        """
        category = self._get_category(category)
        path = 'posts/{category}/{username}'.format(category=category, username=self.username)

        response = self._request(path, kwargs)
        return response

    def collections(self, category=None, **kwargs):
        """
        Get a list of collections by the user.

        Args:
            category: The category of the desired data.
                (Options: 'public' | 'popular' | 'loved')
                (Default: 'popular')
            page: The page number of the desired data. (Default: 1)

        Returns:
            A list of collections (dicts) returned from the API.
        """
        category = self._get_category(category)
        path = 'collections/{category}/{username}'.format(category=category, username=self.username)

        response = self._request(path, kwargs)
        return response
