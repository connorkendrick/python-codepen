# Only call from tests/ directory

import vcr
from .response_tests import response_test_list
from codepen import Posts

"""
Constants
"""
CATEGORY = 'picks'
PAGE = 2

posts_instance = Posts()

@vcr.use_cassette('vcr_cassettes/posts.yml')
def test_posts_list(post_keys):
    """Tests an API call to get a list of posts"""

    response = posts_instance.list(category=CATEGORY, page=PAGE)

    response_test_list(response, post_keys)
