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

            Keys for profile data:
                [nicename]: The user's actual name.
                [username]: The user's username.
                [avatar]: Link to the user's avatar image.
                [location]: User's location.
                [bio]: User's bio description.
                [pro]: Whether user is CodePen Pro member. (True/False)
                [followers]: Number of followers.
                [following]: Number of users that user is following.
                [links]: Social links provided by the user. (list)
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

            Keys for following/followers data:
                [nicename]: The user's actual name.
                [username]: The user's username.
                [avatar]: Link to the user's avatar image.
                [url]: Link to user's profile.
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

            Keys for following/followers data:
                [nicename]: The user's actual name.
                [username]: The user's username.
                [avatar]: Link to the user's avatar image.
                [url]: Link to user's profile.
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

            Keys for tag data:
                [tag]: The tag used on pens by the user.
                [penCount]: Number of pens matching tag.
                [link]: Link to list of pens matching tag.
                [user]: User's username.
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

            Keys for user pen data:
                [title]: Title of the pen.
                [details]: Details of the pen.
                [link]: Link to the pen.
                [id]: Pen's ID.
                [views]: Number of views.
                [loves]: Number of loves.
                [comments]: Number of comments.
                [images]: Image data for the pen. (dict)
                    Keys for images:
                        [small]: Small image of pen.
                        [large]: Large image of pen.
                [user]: User data for the pen. (dict)
                    Keys for user:
                        [nicename]: The user's actual name.
                            (Only available in 'loved' category)
                        [username]: The user's username.
                        [avatar]: Link to the user's avatar image.
                            (Only available in 'loved' category)
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

            Keys for user post data:
                [title]: Title of the post.
                [content]: Content of the post.
                [link]: Link to the post.
                [views]: Number of views.
                [loves]: Number of loves.
                [comments]: Number of comments.
                [user]: User data for the post. (dict)
                    Keys for user:
                        [nicename]: The user's actual name.
                            (Only available in 'loved' category)
                        [username]: The user's username.
                        [avatar]: Link to the user's avatar image.
                            (Only available in 'loved' category)
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

             Keys for collection data:
                [title]: Title of the collection.
                [details]: Details of the collection.
                [id]: Collection's ID.
                [url]: Link to the collection.
                [penCount]: Number of pens in collection.
                [loves]: Number of loves.
                [views]: Number of views.
                [user]: User data for the collection. (dict)
                    Keys for user:
                        [nicename]: The user's actual name.
                            (Only available in 'loved' category)
                        [username]: The user's username.
                        [avatar]: Link to the user's avatar image.
                            (Only available in 'loved' category)
                        [profileUrl]: Link to the user's profile.
                            (Only available in 'loved' category)
        """
        category = self._get_category(category)
        path = 'collections/{category}/{username}'.format(category=category, username=self.username)

        response = self._request(path, kwargs)
        return response
