import pytest
from app import app 

@pytest.fixture
def client():
    
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client 


def test_1_get_items_happy_path(client):
    """Testa se a rota /items retorna status 200 e o conteúdo correto."""
    response = client.get('/items')
    
    assert response.status_code == 200
    
    
    expected_data = {"items": ["item1", "item2", "item3"]}
    assert response.get_json() == expected_data


def test_2_protected_route_unauthorized_error(client):
    """Testa se a rota /protected retorna 401 quando o token está ausente."""
    response = client.get('/protected')
    

    assert response.status_code == 401


def test_3_login_generates_token(client):
    """Testa se a rota /login gera e retorna um token de acesso válido."""
    response = client.post('/login')
    data = response.get_json()
    
    
    assert response.status_code == 200
    
    
    assert 'access_token' in data
    
    
    assert len(data['access_token']) > 0


def test_4_protected_route_access_granted(client):
    """Testa se a rota /protected é acessível com um token válido."""
    
    login_response = client.post('/login')
    token = login_response.get_json()['access_token']
    
    
    protected_response = client.get('/protected', headers={
        'Authorization': f'Bearer {token}'
    })
    
    assert protected_response.status_code == 200
    assert protected_response.get_json()['message'] == "Protected route"