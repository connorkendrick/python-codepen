# Only call from tests/ directory

import vcr
from codepen import Pens

"""
Constants
"""
CATEGORY = 'popular'
TAG = 'css'
PAGE = 2

@vcr.use_cassette('vcr_cassettes/pens.yml')
def test_pens_list(pen_keys):
    """Tests an API call to get a list of pens"""

    pens_instance = Pens()

    response = pens_instance.list(category=CATEGORY, page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(pen_keys).issubset(response[0].keys()), "All keys should be in the response"

@vcr.use_cassette('vcr_cassettes/pens_tag.yml')
def test_pens_tag(pen_keys):
    """Tests an API call to get a list of pens"""

    pens_instance = Pens()

    response = pens_instance.tag(tag=TAG, page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(pen_keys).issubset(response[0].keys()), "All keys should be in the response"
