import vcr
from .response_tests import response_test_list
from codepen import Collections

"""
Constants
"""
ID = 'amheq'
CATEGORY = 'picks'
PAGE = 2

collections_instance = Collections()

@vcr.use_cassette('vcr_cassettes/collection_info.yml')
def test_collection_info(collection_info_keys):
    """Tests an API call to get info for a collection"""

    response = collections_instance.collection_info(collection_id=ID, page=PAGE)

    response_test_list(response, collection_info_keys)

@vcr.use_cassette('vcr_cassettes/collections.yml')
def test_collections_list(collections_list_keys):
    """Tests an API call to get a list of collections"""

    response = collections_instance.list(category=CATEGORY, page=PAGE)

    response_test_list(response, collections_list_keys)
