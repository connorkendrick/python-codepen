from .base import CodePen

class User(CodePen):
    def __init__(self, username):
        super(User, self).__init__()
        self.username = username

    def profile(self):
        """
        Get the profile data for the user.

        Returns:
            A dict representation of the JSON 'data' key returned from the API.
        """
        path = 'profile/{username}'.format(username=self.username)

        response = self._GET(path)
        return response
        
    def following_list(self, **kwargs):
        """
        Get a list of users the user is following.

        Args:
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'following/{username}'.format(username=self.username)

        response = self._GET(path, kwargs)
        return response

    def follower_list(self, **kwargs):
        """
        Get a list of users that follow the user.

        Args:
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'followers/{username}'.format(username=self.username)

        response = self._GET(path, kwargs)
        return response

    def user_tags(self, **kwargs):
        """
        Get a list of tags for the user.

        Args:
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        path = 'tags/{username}'.format(username=self.username)

        response = self._GET(path, kwargs)
        return response

    def pens(self, category=None, **kwargs):
        """
        Get a list of pens by the user.

        Args:
            category: 'public' | 'popular' | 'loved' | 'forked' | 'showcase'
                (default: 'popular')
            tag: The tag of the desired data.
                (optional)
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        category = self._get_category(category)
        path = 'pens/{category}/{username}'.format(category=category, username=self.username)

        response = self._GET(path, kwargs)
        return response

    def posts(self, category=None, **kwargs):
        """
        Get a list of posts by the user.

        Args:
            category: 'published' | 'popular' | 'loved'
                (default: 'popular')
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        category = self._get_category(category)
        path = 'posts/{category}/{username}'.format(category=category, username=self.username)

        response = self._GET(path, kwargs)
        return response

    def collections(self, category=None, **kwargs):
        """
        Get a list of collections by the user.

        Args:
            category: 'public' | 'popular' | 'loved'
                (default: 'popular')
            page: The page number of the desired data.
                (default: 1)

        Returns:
            A list representation of the JSON 'data' key returned from the API.
        """
        category = self._get_category(category)
        path = 'collections/{category}/{username}'.format(category=category, username=self.username)

        response = self._GET(path, kwargs)
        return response
