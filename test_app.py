import pytest
from app import app # Importa a instância 'app' do seu app.py

# 1. FIXTURE: Cria um cliente de teste para simular requisições HTTP
@pytest.fixture
def client():
    # Configura o Flask para modo de teste
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client # Retorna o cliente para os testes usarem

# =================================================================
# TIPO 1: Caminho Feliz (Happy Path)
# Testa uma rota pública que deve ter sucesso (HTTP 200)
# =================================================================
def test_1_get_items_happy_path(client):
    """Testa se a rota /items retorna status 200 e o conteúdo correto."""
    response = client.get('/items')
    
    # Verifica o status code
    assert response.status_code == 200
    
    # Verifica o conteúdo da resposta
    expected_data = {"items": ["item1", "item2", "item3"]}
    assert response.get_json() == expected_data

# =================================================================
# TIPO 2: Teste de Exceção/Erro (401 Unauthorized)
# Testa uma rota protegida sem enviar o token JWT
# =================================================================
def test_2_protected_route_unauthorized_error(client):
    """Testa se a rota /protected retorna 401 quando o token está ausente."""
    response = client.get('/protected')
    
    # Verifica o status code 401 Unauthorized
    assert response.status_code == 401

# =================================================================
# TIPO 3: Condição de Contorno/Comportamento Específico (Geração de Token)
# Testa se a rota /login retorna um token de acesso
# =================================================================
def test_3_login_generates_token(client):
    """Testa se a rota /login gera e retorna um token de acesso válido."""
    response = client.post('/login')
    data = response.get_json()
    
    # Verifica o status code
    assert response.status_code == 200
    
    # Verifica se o campo 'access_token' existe
    assert 'access_token' in data
    
    # Verifica se o token não é uma string vazia
    assert len(data['access_token']) > 0

# Teste adicional (OPCIONAL, mas bom) para garantir que a rota protegida funciona com token
def test_4_protected_route_access_granted(client):
    """Testa se a rota /protected é acessível com um token válido."""
    # 1. Fazer login para obter um token
    login_response = client.post('/login')
    token = login_response.get_json()['access_token']
    
    # 2. Fazer requisição para a rota protegida com o token no header
    protected_response = client.get('/protected', headers={
        'Authorization': f'Bearer {token}'
    })
    
    assert protected_response.status_code == 200
    assert protected_response.get_json()['message'] == "Protected route"