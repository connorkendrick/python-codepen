# Only call from tests/ directory

import vcr
from pytest import fixture
from codepen import Posts

"""
Constants
"""
CATEGORY = 'popular'
PAGE = 2

@fixture
def post_keys():
    # Responsible only for returning the test data (keys for posts)
    return ['title', 'content', 'link', 'views', 'loves', 'comments', 'user']

@vcr.use_cassette('vcr_cassettes/posts.yml')
def test_posts_list(post_keys):
    """Tests an API call to get a list of posts"""

    response = Posts.list(CATEGORY, PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(post_keys).issubset(response[0].keys()), "All keys should be in the response"
