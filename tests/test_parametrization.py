import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 0, 3, -2])
def test_number(number: int):
    print("Number:", number)


@pytest.mark.parametrize('a, b, expected',
                         [
                             (2, 1, 2),
                             (4, 2, 8),
                             (6, 3, 18),
                             (8, 4, 32)
                         ]
                         )
def test_several_numbers(a: int, b: int, expected: int):
    assert a * b


@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
@pytest.mark.parametrize('os', ['windows', 'linux', 'macos'])
def test_cross_browsers_cross_platforms(os: str, browser: str):
    assert len(os + browser) > 11


@pytest.mark.parametrize("data", [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    {"username": "admin", "password": "admin123"},
],
                         ids=[
                             'active user',
                             'blocked user',
                             'new user'
                         ])
def test_login(data):
    assert len(data["username"] + data["password"]) > 0


@pytest.fixture(params=["chrome", "firefox", "safari"])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alex', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account):
        print(f'User with operations: {user}')

    def test_user_without_operations(self, user: str):
        print(f'User without operations: {user}')


users = {
    '+372291001011': 'User with active account',
    '+372291001022': 'User with blocked account',
    '+372291001033': 'User with negative balance on account'}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...
