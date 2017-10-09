import vcr
from .response_tests import response_test_list, response_test_dict
from codepen import User

"""
Constants
"""
USER = 'chriscoyier'
PENS_CATEGORY = 'public'
POSTS_CATEGORY = 'published'
COLLECTIONS_CATEGORY = 'loved'
TAG = 'css'
PAGE = 2

user_instance = User(USER)

@vcr.use_cassette('vcr_cassettes/user_profile.yml')
def test_user_profile(profile_keys):
    """Tests an API call to get a user's profile data"""

    response = user_instance.profile()

    response_test_dict(response, profile_keys)
    assert response['username'] == USER, "The username should be in the response"

@vcr.use_cassette('vcr_cassettes/following_list.yml')
def test_user_following_list(follow_keys):
    """Tests an API call to get a list of users that the user is following"""
    
    response = user_instance.following_list(page=PAGE)

    response_test_list(response, follow_keys)

@vcr.use_cassette('vcr_cassettes/follower_list.yml')
def test_user_follower_list(follow_keys):
    """Tests an API call to get a list of user's followers"""

    response = user_instance.follower_list(page=PAGE)

    response_test_list(response, follow_keys)

@vcr.use_cassette('vcr_cassettes/user_tags.yml')
def test_user_tags(user_tags_keys):
    """Tests an API call to get a list of tags by a user"""

    response = user_instance.user_tags(page=PAGE)

    response_test_list(response, user_tags_keys)

@vcr.use_cassette('vcr_cassettes/user_pens.yml')
def test_user_pens(pen_keys):
    """Tests an API call to get a list of pens by a user"""

    response = user_instance.pens(category=PENS_CATEGORY, tag=TAG, page=PAGE)

    response_test_list(response, pen_keys)

@vcr.use_cassette('vcr_cassettes/user_posts.yml')
def test_user_posts(post_keys):
    """Tests an API call to get a list of posts by a user"""

    response = user_instance.posts(category=POSTS_CATEGORY, page=PAGE)

    response_test_list(response, post_keys)

@vcr.use_cassette('vcr_cassettes/user_collections.yml')
def test_user_collections(collections_list_keys):
    """Tests an API call to get a list of collections by a user"""

    response = user_instance.collections(category=COLLECTIONS_CATEGORY, page=PAGE)

    response_test_list(response, collections_list_keys)
