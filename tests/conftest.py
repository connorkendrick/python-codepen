from pytest import fixture

@fixture(scope='module')
def pen_keys():
    return ['title', 'details', 'link', 'id', 'views', 'loves',
            'comments', 'images', 'user']

@fixture(scope='module')
def post_keys():
    return ['title', 'content', 'link', 'views', 'loves',
            'comments', 'user']

@fixture(scope='module')
def collection_info_keys():
    return ['title', 'details', 'link', 'id', 'views', 'loves',
            'comments', 'images', 'user']

@fixture(scope='module')
def collections_list_keys():
    return ['title', 'details', 'id', 'url', 'penCount', 'loves',
            'views', 'user']

@fixture(scope='module')
def profile_keys():
    return ['nicename', 'username', 'avatar', 'location', 'bio',
            'pro', 'followers', 'following', 'links']

@fixture(scope='module')
def follow_keys():
    return ['nicename', 'username', 'avatar', 'url']

@fixture(scope='module')
def user_tags_keys():
    return ['tag', 'penCount', 'link', 'user']
