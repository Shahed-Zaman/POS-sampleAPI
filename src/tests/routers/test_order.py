from starlette.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_order_no_body():
    response = client.post("/order/")
    assert response.status_code == 422, response.text

def test_create_order():
    # Add a valid item id from all the items in menu
    response = client.post("/menu/", json={"price":999, "quantity":999, "description":"TestCase: test_create_order"} )
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

    global createdOrder
    response = client.post("/order/", json=testOrder )
    assert response.status_code == 201, response.text
    createdOrder = response.json()

def test_read_orders():
    response = client.get("/order/")
    assert response.status_code == 200, response.text
    allOrders = response.json()
    assert len(allOrders) >= 1

def test_read_order():
    global createdOrder
    id = createdOrder['orderid']
    response = client.get("/order/%s" %id)
    assert response.status_code == 200, response.text
    assert response.json()['id'] == id


