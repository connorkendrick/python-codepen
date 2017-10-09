def response_test_list(response, fixture):
    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(fixture).issubset(response[0].keys()), "All keys should be in the response data"

def response_test_dict(response, fixture):
    assert isinstance(response, dict), "The response should be a dict instance"
    assert set(fixture).issubset(response.keys()), "All keys should be in the response"
