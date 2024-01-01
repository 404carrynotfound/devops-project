import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert b'Hello, welcome to the Flask app!' in response.data

def test_goodbye_endpoint(client):
    response = client.get('/goodbye')
    assert response.status_code == 200
    assert b'Goodbye! Thanks for visiting.' in response.data
