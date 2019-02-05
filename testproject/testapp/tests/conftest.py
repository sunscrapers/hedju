import pytest

from .factories import ExampleFactory

BATCH_SIZE = 231


@pytest.fixture(autouse=True)
def example_data():
    ExampleFactory.create_batch(size=BATCH_SIZE)
