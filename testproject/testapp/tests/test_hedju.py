import pytest
from django.test.testcases import TestCase

from .factories import ExampleFactory

pytestmark = pytest.mark.django_db

BATCH_SIZE = 231


class HedjuTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        ExampleFactory.create_batch(size=BATCH_SIZE)
        super().setUpClass()

    def test_001_endpoint(self):
        result = self.client.get('/examples/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(len(result.data), BATCH_SIZE)

    def test_002_limitoffset(self):
