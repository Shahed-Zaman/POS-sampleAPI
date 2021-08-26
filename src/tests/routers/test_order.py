from starlette.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_create_order_no_body():
    response = client.post("/order/")
    assert response.status_code == 422, response.text


def test_create_order():
    # Add a valid item id from all the items in menu
    response = client.post("/menu/", json={"price": 999, "quantity": 999, "description": "TestCase: test_create_order"})
    assert response.status_code == 201, response.text
    menuItemId = response.json()["id"]
    testOrder = {
        "items": [
            {
                "id": menuItemId,
                "quantity": 999
            }
        ],
        "note": "Test case: test_create_order"
    }

    global createdOrderId
    response = client.post("/order/", json=testOrder)
    assert response.status_code == 201, response.text
    createdOrderId = response.json()


def test_get_orders():
    response = client.get("/order/")
    assert response.status_code == 200, response.text
    allOrders = response.json()
    assert len(allOrders) >= 1


def test_get_order():
    global createdOrderId
    response = client.get("/order/%s" % createdOrderId)
    assert response.status_code == 200, response.text
    assert response.json()['id'] == createdOrderId


def test_create_order_low_payment():
    # Add a valid item id from all the items in menu
    response = client.post("/menu/",
                           json={"price": 10, "quantity": 10, "description": "TestCase: test_create_order_low_payment"})
    assert response.status_code == 201, response.text
    menuItemId = response.json()["id"]
    testOrder = {
        "items": [
            {
                "id": menuItemId,
                "quantity": 10
            }
        ],
        "note": "Test case: test_create_order",
        "payment": 99.99
    }

    global createdOrderId
    response = client.post("/order/", json=testOrder)
    assert response.status_code == 422, response.text
    createdOrderId = response.json()


def test_create_order_low_inventory():
    # Add a valid item id from all the items in menu
    response = client.post("/menu/",
                           json={"price": 10, "quantity": 10, "description": "TestCase: test_create_order_low_payment"})
    assert response.status_code == 201, response.text
    menuItemId = response.json()["id"]
    testOrder = {
        "items": [
            {
                "id": menuItemId,
                "quantity": 11
            }
        ],
        "note": "Test case: test_create_order",
        "payment": 500
    }

    global createdOrderId
    response = client.post("/order/", json=testOrder)
    assert response.status_code == 500, response.text
    createdOrderId = response.json()
