# Only call from tests/ directory

import vcr
from pytest import fixture
from codepen import Search

"""
Constants
"""
QUERY = 'CSS'
USER = 'chriscoyier'
PAGE = 2

@fixture
def pen_keys():
    # Responsible only for returning the test data (keys for pens)
    return ['title', 'details', 'link', 'id', 'views', 'loves', 'comments', 'images', 'user']

@vcr.use_cassette('vcr_cassettes/search_pens.yml')
def test_search_pens(pen_keys):
    """Tests an API call to get a list of pens"""

    response = Search.pens(QUERY, USER, PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(pen_keys).issubset(response[0].keys()), "All keys should be in the response"

@fixture
def post_keys():
    # Responsible only for returning the test data (keys for posts)
    return ['title', 'content', 'link', 'views', 'loves', 'comments', 'user']

@vcr.use_cassette('vcr_cassettes/search_posts.yml')
def test_search_posts(post_keys):
    """Tests an API call to get a list of posts"""

    response = Search.posts(QUERY, PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(post_keys).issubset(response[0].keys()), "All keys should be in the response"

@fixture
def collection_keys():
    # Responsible only for returning the test data (keys for collections)
    return ['title', 'details', 'id', 'url', 'penCount', 'loves', 'views', 'user']

@vcr.use_cassette('vcr_cassettes/search_collections.yml')
def test_search_collections(collection_keys):
    """Tests an API call to get a list of collections"""

    response = Search.collections(QUERY, PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(collection_keys).issubset(response[0].keys()), "All keys should be in the response"
