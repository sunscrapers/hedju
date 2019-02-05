import pytest
from factory.django import DjangoModelFactory


class ExampleFactory(DjangoModelFactory):
    class Meta:
        model = 'testapp.Example'


@pytest.fixture
def example_data():
    ExampleFactory.create_batch(size=231)
