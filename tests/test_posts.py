"""This module provides tests for the Posts functionality."""
import vcr

from codepen import Posts
from .response_tests import response_test_list


# Constants
CATEGORY = 'picks'
PAGE = 2


# An instance of Posts
Posts.posts_instance = Posts()


@vcr.use_cassette('vcr_cassettes/posts.yml')
def test_posts_list(post_keys):
    """Tests an API call to get a list of posts"""

    response = Posts.posts_instance.list(category=CATEGORY, page=PAGE)
    response_test_list(response, post_keys)
