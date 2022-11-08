from src.client import Client, UnknownAPIFormatError
import pytest

@pytest.fixture
def params():
    params = {}
    params['url'] = 'foo'
    params['access_token'] = 'bar'
    params['api_path'] = 'foo2'
    yield params


def test_client_raises_unknown_api_when_wrong_api(params):
    """
    Raises uknown API when no API is parsed
    """
    with pytest.raises(UnknownAPIFormatError) as APIFormatError:
        client = Client(params['url'], params['access_token'], '/badApipath')
    assert APIFormatError.value.args == ('"/badApipath" is not a recognized API path.',)

# def test_client_raises_when_no_json():
#     """
#     Raises uknown API when no API is parsed
#     """
#     client = Client(params['url'], params['access_token'], '/badApipath')
#     with pytest.raises(UnknownAPIFormatError) as APIFormatError:
#         client = Client(params['url'], params['access_token'], '/badApipath')
#         client._request(False, 'GET')


# def test_simple_mocking(mocker):
#     """
#     pytest-mock provides a fixture for easy, self-cleaning mocking
#     """
#     mock_db_service = mocker.patch("other_code.services.db_service", autospec=True)

#     mock_data = [(0, "fake row", 0.0)]

#     mock_db_service.return_value = mock_data

#     print("\n(Calling count_service with the DB mocked out...)")

#     c = count_service("foo")

#     mock_db_service.assert_called_with("foo")

#     assert c == 1