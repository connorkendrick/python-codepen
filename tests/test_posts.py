# Only call from tests/ directory

import vcr
from codepen import Posts

"""
Constants
"""
CATEGORY = 'popular'
PAGE = 2

posts_instance = Posts()

@vcr.use_cassette('vcr_cassettes/posts.yml')
def test_posts_list(post_keys):
    """Tests an API call to get a list of posts"""

    response = posts_instance.list(category=CATEGORY, page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(post_keys).issubset(response[0].keys()), "All keys should be in the response"
