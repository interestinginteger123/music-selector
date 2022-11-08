import pytest
from src.client2 import  LyricsClient, NoAccessToken

@pytest.fixture
def params():
    params = {}
    params['token'] = 'foo'
    yield params


def test_client_raises_unknown_api_when_wrong_api(params):
    """
    Raises uknown API when no Token is parsed
    """
    with pytest.raises(TypeError) as noAccessToken:
        lyricsclient = LyricsClient(None)
    assert noAccessToken.value.args == ('Invalid token',)



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