# Only call from tests/ directory

import vcr
from pytest import fixture
from codepen import User

@fixture
def profile_keys():
    # Responsible only for returning the test data (keys for user profile data)
    return ['nicename', 'username', 'avatar', 'location', 'bio', 'pro', 'followers', 'following', 'links']

@vcr.use_cassette('vcr_cassettes/user_profile.yml')
def test_user_profile(profile_keys):
    """Tests an API call to get a user's profile data"""

    user_instance = User("connorkendrick")
    response = user_instance.profile()

    assert isinstance(response, dict)
    assert response['username'] == "connorkendrick", "The username should be in the response"
    assert set(profile_keys).issubset(response.keys()), "All keys should be in the response"

@fixture
def follow_keys():
    # Responsible only for returning the test data (keys for list of users that a user is following)
    return ['nicename', 'username', 'avatar', 'url']

@vcr.use_cassette('vcr_cassettes/following_list.yml')
def test_user_following_list(follow_keys):
    """Tests an API call to get a list of users that the user is following"""
    
    user_instance = User("connorkendrick")
    response = user_instance.following_list()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(follow_keys).issubset(response[0].keys())

@vcr.use_cassette('vcr_cassettes/follower_list.yml')
def test_user_follower_list(follow_keys):
    """Tests an API call to get a list of user's followers"""

    user_instance = User("chriscoyier")
    response = user_instance.follower_list(page=2)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(follow_keys).issubset(response[0].keys())

@fixture
def user_tags_keys():
    # Responsible only for returning the test data (keys for a user tag list)
    return ['tag', 'penCount', 'link', 'user']

@vcr.use_cassette('vcr_cassettes/user_tags.yml')
def test_user_tags(user_tags_keys):
    """Tests an API call to get a list of tags by a user"""

    user_instance = User("chriscoyier")
    response = user_instance.user_tags()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(user_tags_keys).issubset(response[0].keys())
