import vcr
from .response_tests import response_test_list
from codepen import Pens

"""
Constants
"""
CATEGORY = 'picks'
TAG = 'css'
PAGE = 2

pens_instance = Pens()

@vcr.use_cassette('vcr_cassettes/pens.yml')
def test_pens_list(pen_keys):
    """Tests an API call to get a list of pens"""

    response = pens_instance.list(category=CATEGORY, page=PAGE)

    response_test_list(response, pen_keys)

@vcr.use_cassette('vcr_cassettes/pens_tag.yml')
def test_pens_tag(pen_keys):
    """Tests an API call to get a list of pens"""

    response = pens_instance.tag(tag=TAG, page=PAGE)

    response_test_list(response, pen_keys)
