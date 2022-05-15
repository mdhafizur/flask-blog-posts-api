
from app import create_app

app = create_app()
client = app.test_client()


def test_ping():
    response = client.get('/api/ping/')
    assert response.status_code == 200


def test_with_valid_sort_by():
    for sort in ["id", "reads", "likes", "popularity"]:
        response = client.get(f'/api/posts/?tags=tech&sortBy={sort}')
        if response.status_code != 200:
            break
    assert response.status_code == 200


def test_with_valid_directions():
    for sort in ["asc", "desc"]:
        response = client.get(f'/api/posts/?tags=tech&direction={sort}')
        if response.status_code != 200:
            break
    assert response.status_code == 200


def test_with_no_tags():
    response = client.get('/api/posts/')
    assert response.status_code == 400


def test_with_wrong_sort_by():
    response = client.get('/api/posts/?tags=tech&sortBy=as')
    assert response.status_code == 400


def test_with_wrong_direction():
    response = client.get('/api/posts/?tags=tech&direction=as')
    assert response.status_code == 400
