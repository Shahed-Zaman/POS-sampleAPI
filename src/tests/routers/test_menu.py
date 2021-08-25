from starlette.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_menuitem_no_body():
    response = client.post("/menu/")
    assert response.status_code == 422, response.text

def test_create_menuitem():
    global createdMenuItem
    response = client.post("/menu/", json={"price":999, "quantity":999, "description":"TestCase: test_create_menuitem_valid"} )
    assert response.status_code == 201, response.text
    createdMenuItem = response.json()

def test_read_menu():
    response = client.get("/menu/")
    assert response.status_code == 200, response.text
    allMenuItems = response.json()
    assert len(allMenuItems) >= 1

def test_read_menuitem():
    global createdMenuItem
    id = createdMenuItem['id']
    response = client.get("/menu/%s" %id)
    assert response.status_code == 200, response.text
    assert response.json()['id'] == id

def test_update_menuitem():
    global createdMenuItem
    id = createdMenuItem['id']
    response = client.put("/menu/", json={"price":999, "quantity":1000, "description":"TestCase: test_update_menuitem", "id": id} )
    assert response.status_code == 204, response.text

def test_delete_menuitem():
    global createdMenuItem
    deleteId = createdMenuItem['id']
    response = client.delete("/menu/%s" %deleteId)
    assert response.status_code == 200, response.text

def test_read_menuitem_when_not_present():
    global createdMenuItem
    id = createdMenuItem['id']
    response = client.get("/menu/%s" %id)
    assert response.status_code == 404, response.text

def test_delete_menuitem_when_not_present():
    global createdMenuItem
    deleteId = createdMenuItem['id']
    response = client.delete("/menu/%s" %deleteId)
    assert response.status_code == 404, response.text


