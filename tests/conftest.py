import pytest
from faker import Faker
from django.urls import reverse
from elibrary_app.models import Catalog


fake = Faker()  # Создаем экземпляр Faker
Faker.seed(42)  # Для воспроизводимости результатов


@pytest.fixture
def home_response(client):
    """Возвращает response для страницы home"""
    return client.get(reverse('home'))


@pytest.fixture
def book():
    """Создает одну НЕсохраненную книгу"""
    return Catalog(
        title='First Django Book',
        ISBN='978-1-60309-3',
        author='Ilya Perminov',
        price='9.99',
        availability='True'
    )


@pytest.fixture
def faker_several_books():
    """Создает несколько НЕсохраненных книг"""
    return [
        Catalog(
            title=fake.catch_phrase(),
            ISBN=fake.isbn13(),
            author=fake.name(),
            price=str(round(fake.pydecimal(left_digits=2, right_digits=2, positive=True), 2)),
            availability=fake.boolean()
        )
        for _ in range(5)
    ]
