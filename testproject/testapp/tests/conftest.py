import pytest

from .factories import ExampleFactory


@pytest.fixture(autouse=True)
def example_data():
    ExampleFactory.create_batch(size=231)
