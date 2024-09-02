import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/refeicoes"

# Helper function to create a valid refeicao
def create_refeicao(payload):
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    return response.json()['id']

def test_create_refeicao():
    payload = {
        "nome": "Almoço de Domingo",
        "descricao": "Frango grelhado com salada",
        "data_hora": "2024-09-02T12:30:00",
        "dentro_dieta": True
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert 'id' in data

def test_get_refeicao():
    id = create_refeicao({
        "nome": "Almoço de Domingo",
        "descricao": "Frango grelhado com salada",
        "data_hora": "2024-09-02T12:30:00",
        "dentro_dieta": True
    })

    response = requests.get(f"{BASE_URL}/{id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == id
    assert data["nome"] == "Almoço de Domingo"

def test_update_refeicao():
    id = create_refeicao({
        "nome": "Almoço de Domingo",
        "descricao": "Frango grelhado com salada",
        "data_hora": "2024-09-02T12:30:00",
        "dentro_dieta": True
    })

    updated_payload = {
        "nome": "Almoço de Sábado",
        "descricao": "Peixe assado com legumes",
        "data_hora": "2024-09-01T13:00:00",
        "dentro_dieta": False
    }
    response = requests.put(f"{BASE_URL}/{id}", json=updated_payload)
    assert response.status_code == 200
    assert response.json()['message'] == 'Refeição atualizada'

    response = requests.get(f"{BASE_URL}/{id}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Almoço de Sábado"
    assert data["descricao"] == "Peixe assado com legumes"
    assert data["data_hora"] == "2024-09-01T13:00:00"
    assert data["dentro_dieta"] == False

def test_delete_refeicao():
    id = create_refeicao({
        "nome": "Almoço de Domingo",
        "descricao": "Frango grelhado com salada",
        "data_hora": "2024-09-02T12:30:00",
        "dentro_dieta": True
    })

    response = requests.delete(f"{BASE_URL}/{id}")
    assert response.status_code == 200
    assert response.json()['message'] == 'Refeição deletada'

    response = requests.get(f"{BASE_URL}/{id}")
    assert response.status_code == 404
    assert response.json()['error'] == 'Refeição não encontrada'

def test_get_all_refeicoes():
    payloads = [
        {
            "nome": "Almoço de Domingo",
            "descricao": "Frango grelhado com salada",
            "data_hora": "2024-09-02T12:30:00",
            "dentro_dieta": True
        },
        {
            "nome": "Jantar de Domingo",
            "descricao": "Massas com molho",
            "data_hora": "2024-09-02T19:00:00",
            "dentro_dieta": False
        }
    ]

    ids = [create_refeicao(payload) for payload in payloads]

    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= len(payloads)

def test_create_refeicao_missing_fields():
    payload = {
        "descricao": "Descrição sem nome",
        "data_hora": "2024-09-02T12:30:00",
        "dentro_dieta": True
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 400
    assert response.json()['error'] == 'Nome é obrigatório'

def test_get_non_existent_refeicao():
    response = requests.get(f"{BASE_URL}/999")
    assert response.status_code == 404
    assert response.json()['error'] == 'Refeição não encontrada'

def test_update_non_existent_refeicao():
    payload = {
        "nome": "Almoço de Sábado",
        "descricao": "Peixe assado com legumes",
        "data_hora": "2024-09-01T13:00:00",
        "dentro_dieta": False
    }
    response = requests.put(f"{BASE_URL}/999", json=payload)
    assert response.status_code == 404
    assert response.json()['error'] == 'Refeição não encontrada'

def test_delete_non_existent_refeicao():
    response = requests.delete(f"{BASE_URL}/999")
    assert response.status_code == 404
    assert response.json()['error'] == 'Refeição não encontrada'
