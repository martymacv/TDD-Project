import pytest
from elibrary_app.models import Catalog


@pytest.fixture
def sample_books(db):
    """Создает тестовые книги"""
    book1 = Catalog.objects.create(
        title='Django for Beginners (2018)',
        ISBN='978-1-60309-0',
        author='John Doe',
        price=9.99,
        availability=True
    )
    book2 = Catalog.objects.create(
        title='Django for Professionals (2020)', 
        ISBN='978-1-60309-3',
        author='Mary Doe',
        price=11.99,
        availability=False
    )
    return [book1, book2]


@pytest.mark.django_db
class TestsCatalogView:
    """    Тест для представлений    """
    def test_book_list_view(self, sample_books, home_response):
        """Проверяет отображение вновь созданных книг в html"""
        assert 'Django for Professionals (2020)' in home_response.content.decode()
        assert 'John Doe' in home_response.content.decode()
        assert '978-1-60309-3' in home_response.content.decode()
