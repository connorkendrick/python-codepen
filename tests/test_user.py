# Only call from tests/ directory

import vcr
from codepen import User

"""
Constants
"""
USER = 'chriscoyier'
CATEGORY = 'popular'
TAG = 'css'
PAGE = 2

@vcr.use_cassette('vcr_cassettes/user_profile.yml')
def test_user_profile(profile_keys):
    """Tests an API call to get a user's profile data"""

    user_instance = User(USER)
    response = user_instance.profile()

    assert isinstance(response, dict), "The response should be a dict instance"
    assert set(profile_keys).issubset(response.keys()), "All keys should be in the response"
    assert response['username'] == USER, "The username should be in the response"

@vcr.use_cassette('vcr_cassettes/following_list.yml')
def test_user_following_list(follow_keys):
    """Tests an API call to get a list of users that the user is following"""
    
    user_instance = User(USER)
    response = user_instance.following_list(page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(follow_keys).issubset(response[0].keys()), "All keys should be in the response"

@vcr.use_cassette('vcr_cassettes/follower_list.yml')
def test_user_follower_list(follow_keys):
    """Tests an API call to get a list of user's followers"""

    user_instance = User(USER)
    response = user_instance.follower_list(page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(follow_keys).issubset(response[0].keys()), "All keys should be in the response"

@vcr.use_cassette('vcr_cassettes/user_tags.yml')
def test_user_tags(user_tags_keys):
    """Tests an API call to get a list of tags by a user"""

    user_instance = User(USER)
    response = user_instance.user_tags(page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(user_tags_keys).issubset(response[0].keys()), "All keys should be in the response"

@vcr.use_cassette('vcr_cassettes/user_pens.yml')
def test_user_pens(pen_keys):
    """Tests an API call to get a list of pens by a user"""

    user_instance = User(USER)
    response = user_instance.pens(category=CATEGORY, tag=TAG, page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(pen_keys).issubset(response[0].keys()), "All keys should be in the response"

@vcr.use_cassette('vcr_cassettes/user_posts.yml')
def test_user_posts(post_keys):
    """Tests an API call to get a list of posts by a user"""

    user_instance = User(USER)
    response = user_instance.posts(category=CATEGORY, page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(post_keys).issubset(response[0].keys()), "All keys should be in the response"

@vcr.use_cassette('vcr_cassettes/user_collections.yml')
def test_user_collections(collections_list_keys):
    """Tests an API call to get a list of collections by a user"""

    user_instance = User(USER)
    response = user_instance.collections(category=CATEGORY, page=PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(collections_list_keys).issubset(response[0].keys()), "All keys should be in the response"
