import requests
import pytest

BASE_URL = "https://restful-api.dev/"

@pytest.fixture
def sample_object():
    
    payload = {"name": "Test Object", "data": {"key": "value"}}
    response = requests.post(BASE_URL + "objects", json=payload)
    assert response.status_code == 201
    yield response.json()
    
    requests.delete(BASE_URL + f"objects/{response.json()['id']}")

def test_patch_object(sample_object):
    obj_id = sample_object['id']
    patch_payload = {"data": {"updatedKey": "updatedValue"}}
    response = requests.patch(BASE_URL + f"objects/{obj_id}", json=patch_payload)

    assert response.status_code == 200
    assert response.json()['data']['updatedKey'] == "updatedValue", "Patch not applied correctly"
