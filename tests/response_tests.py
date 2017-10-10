"""This module provides tests for asserting that the returned data is correct."""

def response_test_list(response, fixture):
    """Tests that a list of data is returned and that the data is correct."""
    assert isinstance(response, list), "The response should be a list instance"
    assert isinstance(response[0], dict), "The response data should be a dict instance"
    assert set(fixture).issubset(response[0].keys()), "All keys should be in the response data"

def response_test_dict(response, fixture):
    """Tests that the returned data is correct."""
    assert isinstance(response, dict), "The response should be a dict instance"
    assert set(fixture).issubset(response.keys()), "All keys should be in the response"
