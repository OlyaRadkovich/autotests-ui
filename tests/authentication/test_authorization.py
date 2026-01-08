import pytest
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    def test_successful_authorization(
            self, registration_page: RegistrationPage, dashboard_page: DashboardPage, login_page: LoginPage
    ):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_page.registration_form.fill(
            email='user.namename@gmail.com', username='Gargoyle', password='password'
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('Gargoyle')
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email='user.namename@gmail.com', password='password')
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('Gargoyle')
        dashboard_page.sidebar.check_visible()

    creds = {
        ('user.name@gmail.com', 'password'): 'Invalid email and password',
        ('user.name@gmail.com', '  '): 'Invalid email, empty password',
        ('  ', 'password'): 'Empty email, invalid password'
    }

    @pytest.mark.parametrize('email, password',
                             creds.keys(),
                             ids=creds.values())
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    def test_navigate_from_authorization_to_registration(
            self, login_page: LoginPage, registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()
        registration_page.registration_form.check_visible(email="", username="", password="")
