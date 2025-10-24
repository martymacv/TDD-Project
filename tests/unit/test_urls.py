import pytest
from django.urls import reverse, resolve
from elibrary_app.views import home


@pytest.mark.django_db
class TestElibraryURLs:
    """    Тестируем URLs    """

    def test_homepage_url_name(self, home_response):
        """Проверяет, что главная страница возвращает 200"""
        assert home_response.status_code == 200

    def test_root_url_resolves_to_homepage_view(self):
        """Проверяет, что URL разрешается в правильную view"""
        found = resolve('/')
        assert found.func == home
