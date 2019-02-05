import pytest

from .conftest import BATCH_SIZE

pytestmark = pytest.mark.django_db


def test_001_default_settings(client):
    result = client.get('/examples/')
    assert result.status_code == 200
    assert len(result.data) == BATCH_SIZE


@pytest.mark.parametrize("page_size", [100, 50, 20])
def test_002_limitoffset(client, page_size):
    result = client.get('/limit_examples/')
    assert len(result.data) == BATCH_SIZE
    result = client.get('/limit_examples/?limit={}'.format(page_size))
    assert len(result.data) == page_size
    assert result.has_header('link')
    assert str(BATCH_SIZE - page_size) in result['link']  # link to last page
    result = client.get('/limit_examples/?limit={}&offset=30'.format(page_size))
    assert result.has_header('link')
    assert 'first' in result['link']
    assert 'previous' in result['link']
    assert 'next' in result['link']
    assert 'last' in result['link']
    result = client.get('/limit_examples/?limit={}&offset=30&envelope=true'.format(page_size))
    assert result.has_header('link')
    assert 'envelope' in result['link']
    assert 'first' in result['link']
    assert 'previous' in result['link']
    assert 'next' in result['link']
    assert 'last' in result['link']
    assert 'first' in result.data
    assert 'previous' in result.data
    assert 'next' in result.data
    assert 'last' in result.data
    assert 'results' in result.data
    assert len(result.data['results']) == page_size


def test_003_pagenumber(client):
    result = client.get('/page_examples/')
    assert len(result.data) == BATCH_SIZE


def test_004_cursor(client):
    result = client.get('/cursor_examples/')
    assert len(result.data) == BATCH_SIZE
