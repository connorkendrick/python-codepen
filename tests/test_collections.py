# Only call from tests/ directory

import vcr
from pytest import fixture
from codepen import Collections

"""
Constants
"""
ID = 'amheq'
CATEGORY = 'popular'
PAGE = 2

@fixture
def collection_info_keys():
    # Responsible only for returning the test data (keys for a collection)
    return ['title', 'details', 'link', 'id', 'views', 'loves', 'comments', 'images', 'user']

@vcr.use_cassette('vcr_cassettes/collection_info.yml')
def test_collection_info(collection_info_keys):
    """Tests an API call to get info for a collection"""

    response = Collections.collection_info(ID)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(collection_info_keys).issubset(response[0].keys()), "All keys should be in the response"

@fixture
def collections_list_keys():
    # Responsible only for returning the test data (keys for collections list)
    return ['title', 'details', 'id', 'url', 'penCount', 'loves', 'views', 'user']

@vcr.use_cassette('vcr_cassettes/collections.yml')
def test_collections_list(collections_list_keys):
    """Tests an API call to get a list of collections"""

    response = Collections.list(CATEGORY, PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(collections_list_keys).issubset(response[0].keys()), "All keys should be in the response"
