import pytest


@pytest.fixture
def setup_teardown():
    test_data = {"user": "testuser", "password": "testpass"}
    yield test_data

    print("Teardown: clean data and environment")


def test_login(setup_teardown):
    assert setup_teardown["user"] == "testuser"
    assert setup_teardown["password"] == "testpass"


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Send data to analytics service")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Initialize autotest settings")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Create user data once for the test class")


@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Open a browser for each test")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...


class TestAccountFlow():
    def test_user_account(self, settings, user, browser):
        ...
