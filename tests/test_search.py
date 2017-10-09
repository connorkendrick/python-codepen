"""This module provides tests for the Search functionality."""

import vcr

from codepen import Search
from .response_tests import response_test_list


# Constants
QUERY = 'CSS'
USER = 'chriscoyier'
PAGE = 2


# An instance of Search
Search.search_instance = Search()


@vcr.use_cassette('vcr_cassettes/search_pens.yml')
def test_search_pens(pen_keys):
    """Tests an API call to get a list of pens"""

    response = Search.search_instance.pens(q=QUERY, limit=USER, page=PAGE)
    response_test_list(response, pen_keys)


@vcr.use_cassette('vcr_cassettes/search_posts.yml')
def test_search_posts(post_keys):
    """Tests an API call to get a list of posts"""

    response = Search.search_instance.posts(q=QUERY, page=PAGE)
    response_test_list(response, post_keys)


@vcr.use_cassette('vcr_cassettes/search_collections.yml')
def test_search_collections(collections_list_keys):
    """Tests an API call to get a list of collections"""

    response = Search.search_instance.collections(q=QUERY, page=PAGE)
    response_test_list(response, collections_list_keys)
