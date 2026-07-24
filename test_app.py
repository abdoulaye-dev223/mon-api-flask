import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_accueil(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bienvenue" in response.data

def test_hello(client):
    response = client.get('/api/hello')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert 'message' in data

def test_status(client):
    response = client.get('/api/status')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'en ligne'
    assert data['version'] == '1.0'

def test_route_inexistante(client):
    response = client.get('/route-qui-nexiste-pas')
    assert response.status_code == 404