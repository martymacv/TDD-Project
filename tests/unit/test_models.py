import pytest
from copy import deepcopy
from elibrary_app.models import Catalog


@pytest.mark.django_db
class TestCatalogModel:

    def test_create_book(self, book):
        """Тест создания объекта книги"""
        assert isinstance(book, Catalog)

    def test_str_representation(self, book):
        """Тест строкового представления"""
        assert str(book) == "First Django Book"

    def test_saving_and_retrieving_book(self, db, book):
        """Тест сохранения и извлечения книг из БД"""
        # Первая книга
        first_book = deepcopy(book)
        first_book.save()

        # Вторая книга
        second_book = deepcopy(book)
        second_book.title = 'Second Django Book'
        second_book.ISBN = '978-3-60124-1'
        second_book.author = 'Dmitry Seleznev'
        second_book.price = '19.99'
        second_book.availability = 'False'
        second_book.save()

        # Проверяем
        saved_books = Catalog.objects.all()
        assert saved_books.count() == 2
        assert saved_books[0].title == 'First Django Book'
        assert saved_books[1].author == 'Dmitry Seleznev'
