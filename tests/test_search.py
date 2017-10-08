# Only call from tests/ directory

import vcr
from codepen import Search

"""
Constants
"""
QUERY = 'CSS'
USER = 'chriscoyier'
PAGE = 2

@vcr.use_cassette('vcr_cassettes/search_pens.yml')
def test_search_pens(pen_keys):
    """Tests an API call to get a list of pens"""

    search_instance = Search()

    response = search_instance.pens(q=QUERY, limit=USER, page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(pen_keys).issubset(response[0].keys()), "All keys should be in the response"

@vcr.use_cassette('vcr_cassettes/search_posts.yml')
def test_search_posts(post_keys):
    """Tests an API call to get a list of posts"""

    search_instance = Search()

    response = search_instance.posts(q=QUERY, page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(post_keys).issubset(response[0].keys()), "All keys should be in the response"

@vcr.use_cassette('vcr_cassettes/search_collections.yml')
def test_search_collections(collections_list_keys):
    """Tests an API call to get a list of collections"""

    search_instance = Search()

    response = search_instance.collections(q=QUERY, page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(collections_list_keys).issubset(response[0].keys()), "All keys should be in the response"
