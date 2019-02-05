import pytest

pytestmark = pytest.mark.django_db

BATCH_SIZE = 231


def test_001_endpoint(client):
    result = client.get('/examples/')
    assert result.status_code == 200
    assert len(result.data) == BATCH_SIZE


def test_002_limitoffset(client, settings):
    result = client.get('/limit_examples/')
    assert len(result.data) == BATCH_SIZE
    result = client.get('/limit_examples/?limit=100')
    assert len(result.data) == 100
    assert result.has_header('link')
    assert str(BATCH_SIZE - 100) in result['link']  # link to last page
    result = client.get('/limit_examples/?limit=100&offset=30')
    assert result.has_header('link')
    assert 'first' in result['link']
    assert 'previous' in result['link']
    assert 'next' in result['link']
    assert 'last' in result['link']
    result = client.get('/limit_examples/?limit=100&offset=30&envelope=true')
    assert result.has_header('link')
    assert 'first' in result['link']
    assert 'previous' in result['link']
    assert 'next' in result['link']
    assert 'last' in result['link']
    assert 'first' in result.data
    assert 'previous' in result.data
    assert 'next' in result.data
    assert 'last' in result.data
    assert 'results' in result.data
    assert len(result.data['results']) == 100
