import pytest


USING_TEMPLATES = [
    'home.html',
]


@pytest.mark.django_db
class TestsCatalogTemplate:
    """    Тест шаблона    """
    @pytest.mark.parametrize('template', USING_TEMPLATES)
    def test_homepage_template(self, home_response, template):
        """Проверяет наличие шаблона (-ов)"""
        assert any((
            t.name == template
            for t in home_response.templates
        )), f"Template '{template}' not used. Used: {[
            t.name for t in home_response.templates
        ]}"

    def test_homepage_contains_correct_html(
            self, home_response):
        """Проверяет наличие заголовка в html"""
        content = home_response.content.decode('utf-8')
        assert 'E-library Application' in content, "Source not used 'E-library Application'"

    def test_homepage_does_not_contain_incorrect_html(
            self, home_response):
        """Проверяет отсутствие заголовка в html"""
        content = home_response.content.decode('utf-8')
        assert 'Hello World' not in content, "Source used 'Hello World'"
