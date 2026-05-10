from fastapi.testclient import TestClient
from main import app, items

client = TestClient(app)


def setup_function():
    items.clear()


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}


def test_get_items_empty():
    response = client.get("/items")

    assert response.status_code == 200
    assert response.json() == []


def test_add_item():
    response = client.post(
        "/items",
        json={
            "name": "Test item",
            "description": "Test description"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Item added"
    assert response.json()["item"]["name"] == "Test item"


def test_update_item():
    client.post(
        "/items",
        json={
            "name": "Old name",
            "description": "Old description"
        }
    )

    response = client.put(
        "/items/0",
        json={
            "name": "New name",
            "description": "New description"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Item updated"
    assert response.json()["item"]["name"] == "New name"


def test_delete_item():
    client.post(
        "/items",
        json={
            "name": "Item to delete",
            "description": "Will be deleted"
        }
    )

    response = client.delete("/items/0")

    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"


def test_delete_item_not_found():
    response = client.delete("/items/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_create_item_missing_description():
    response = client.post(
        "/items",
        json={
            "name": "Invalid item"
        }
    )

    assert response.status_code == 422