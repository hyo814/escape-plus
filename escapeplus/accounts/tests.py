from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LoginRedirectTests(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(username='tester', password='pass1234')

    def login(self, next_url):
        return self.client.post(
            f"{reverse('accounts:login')}?next={next_url}",
            {'username': 'tester', 'password': 'pass1234'},
        )

    def test_login_ignores_external_next_url(self):
        self.assertRedirects(self.login('https://evil.example/'), '/', fetch_redirect_response=False)

    def test_login_follows_internal_next_url(self):
        self.assertRedirects(self.login('/board/review/'), '/board/review/', fetch_redirect_response=False)
