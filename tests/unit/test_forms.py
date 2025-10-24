import pytest
from faker import Faker
from elibrary_app.forms import AddBookForm


fake = Faker()


@pytest.fixture
def empty_book_form():
    """Создает одну пустую форму"""
    return AddBookForm(data={
        'title': '',
        'ISBN': '',
        'author': '',
        'price': '',
        'availability': ''
    })


@pytest.fixture
def valid_book_form():
    """Создает форму с валидными данными"""
    return AddBookForm(data={
        'title': fake.sentence(nb_words=3),
        'ISBN': fake.isbn13(),
        'author': fake.name(),
        'price': str(fake.random_number(digits=2)) + '.' + str(fake.random_number(digits=2)),
        'availability': fake.random_int(min=0, max=100)
    })


@pytest.mark.django_db
class TestsCatalogForm:

    def test_book_form(self, home_response):
        """Проверяет"""
        form = home_response.context.get('add_book_form')
        assert isinstance(form, AddBookForm), f'{type(form) = }, but expected {type(AddBookForm)}'
        assert 'csrfmiddlewaretoken' in str(home_response.content), f'{str(home_response.content) = }'

    def test_bootstrap_class_used_for_default_styling(
            self, home_response
            ):
        """Проверяет стилизацию формы"""
        form = home_response.context.get('add_book_form')
        assert 'class="form-control"' in form.as_p(), f'{form.as_p() = } expected class="form-control"'

    def test_book_form_validation_for_blank_items(self, empty_book_form):
        """Проверяет валидацию пустой формы"""
        assert not empty_book_form.is_valid()

    @pytest.mark.parametrize('required_field', [])
    def test_book_form_required_fields_errors(
            self, empty_book_form, required_field
            ):
        """Проверяет ошибки в пустых обязательных полях"""
        assert required_field in empty_book_form.errors
        assert 'This field is required' in str(empty_book_form.errors[required_field])

    # def test_book_form_validation_for_valid_items(self, valid_book_form):
    #     """Проверяет валидацию корректно заполенной формы"""
    #     assert valid_book_form.is_valid()
