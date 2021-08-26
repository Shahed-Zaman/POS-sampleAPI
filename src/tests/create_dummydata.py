from starlette.testclient import TestClient
from src.main import app

client = TestClient(app)


items = [{"price":999, "quantity":999, "description":"Sample item 1"}
, {"price":999, "quantity":999, "description":"Sample item 2"}
, {"price":999, "quantity":999, "description":"Sample item 3"}
, {"price":999, "quantity":999, "description":"Sample item 4"}
, {"price":999, "quantity":999, "description":"Sample item 5"}
, {"price":999, "quantity":999, "description":"Sample item 6"}
, {"price":999, "quantity":999, "description":"Sample item 7"}]


orders = [{"items":[{"id":1, "quantity":99}, {"id":2, "quantity":99},{"id":3, "quantity":99}]}
,{"items":[{"id":1, "quantity":99}, {"id":2, "quantity":99},{"id":3, "quantity":99}]}
,{"items":[{"id":1, "quantity":99}, {"id":2, "quantity":99},{"id":3, "quantity":99}]}
,{"items":[{"id":1, "quantity":99}, {"id":2, "quantity":99},{"id":3, "quantity":99}]}]

for item in items:
    client.post("/menu/", json=item)

for order in orders:
    client.post("/order/", json=order)

