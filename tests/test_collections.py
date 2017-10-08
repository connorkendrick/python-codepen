# Only call from tests/ directory

import vcr
from codepen import Collections

"""
Constants
"""
ID = 'amheq'
CATEGORY = 'popular'
PAGE = 2

@vcr.use_cassette('vcr_cassettes/collection_info.yml')
def test_collection_info(collection_info_keys):
    """Tests an API call to get info for a collection"""

    collections_instance = Collections()

    response = collections_instance.collection_info(ID=ID)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(collection_info_keys).issubset(response[0].keys()), "All keys should be in the response"

@vcr.use_cassette('vcr_cassettes/collections.yml')
def test_collections_list(collections_list_keys):
    """Tests an API call to get a list of collections"""

    collections_instance = Collections()

    response = collections_instance.list(category=CATEGORY, page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(collections_list_keys).issubset(response[0].keys()), "All keys should be in the response"
