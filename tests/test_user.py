# Only call from tests/ directory

import vcr
from pytest import fixture
from codepen import User

"""
Constants
"""
USER = 'chriscoyier'
CATEGORY = 'popular'
TAG = 'css'
PAGE = 2

@fixture
def profile_keys():
    # Responsible only for returning the test data (keys for user profile data)
    return ['nicename', 'username', 'avatar', 'location', 'bio', 'pro', 'followers', 'following', 'links']

@vcr.use_cassette('vcr_cassettes/user_profile.yml')
def test_user_profile(profile_keys):
    """Tests an API call to get a user's profile data"""

    user_instance = User(USER)
    response = user_instance.profile()

    assert isinstance(response, dict), "The response should be a dict instance"
    assert set(profile_keys).issubset(response.keys()), "All keys should be in the response"
    assert response['username'] == USER, "The username should be in the response"

@fixture
def follow_keys():
    # Responsible only for returning the test data (keys for list of users that a user is following)
    return ['nicename', 'username', 'avatar', 'url']

@vcr.use_cassette('vcr_cassettes/following_list.yml')
def test_user_following_list(follow_keys):
    """Tests an API call to get a list of users that the user is following"""
    
    user_instance = User(USER)
    response = user_instance.following_list(PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(follow_keys).issubset(response[0].keys()), "All keys should be in the response"

@vcr.use_cassette('vcr_cassettes/follower_list.yml')
def test_user_follower_list(follow_keys):
    """Tests an API call to get a list of user's followers"""

    user_instance = User(USER)
    response = user_instance.follower_list(PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(follow_keys).issubset(response[0].keys()), "All keys should be in the response"

@fixture
def user_tags_keys():
    # Responsible only for returning the test data (keys for a user tag list)
    return ['tag', 'penCount', 'link', 'user']

@vcr.use_cassette('vcr_cassettes/user_tags.yml')
def test_user_tags(user_tags_keys):
    """Tests an API call to get a list of tags by a user"""

    user_instance = User(USER)
    response = user_instance.user_tags(PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(user_tags_keys).issubset(response[0].keys()), "All keys should be in the response"

@fixture
def user_pen_keys():
    # Responsible only for returning the test data (keys for a user's pens)
    return ['title', 'details', 'link', 'id', 'views', 'loves', 'comments', 'images', 'user']

@vcr.use_cassette('vcr_cassettes/user_pens.yml')
def test_user_pens(user_pen_keys):
    """Tests an API call to get a list of pens by a user"""

    user_instance = User(USER)
    response = user_instance.pens(CATEGORY, TAG, PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(user_pen_keys).issubset(response[0].keys()), "All keys should be in the response"

@fixture
def user_post_keys():
    # Responsible only for returning the test data (keys for a user's posts)
    return ['title', 'content', 'link', 'views', 'loves', 'comments', 'user']

@vcr.use_cassette('vcr_cassettes/user_posts.yml')
def test_user_posts(user_post_keys):
    """Tests an API call to get a list of posts by a user"""

    user_instance = User(USER)
    response = user_instance.posts(CATEGORY, PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(user_post_keys).issubset(response[0].keys()), "All keys should be in the response"

@fixture
def user_collection_keys():
    # Responsible only for returning the test data (keys for a user's collections)
    return ['title', 'details', 'id', 'url', 'penCount', 'loves', 'views', 'user']

@vcr.use_cassette('vcr_cassettes/user_collections.yml')
def test_user_collections(user_collection_keys):
    """Tests an API call to get a list of collections by a user"""

    user_instance = User(USER)
    response = user_instance.collections(CATEGORY, PAGE)

    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(user_collection_keys).issubset(response[0].keys()), "All keys should be in the response"
