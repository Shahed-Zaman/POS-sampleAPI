from starlette.testclient import TestClient

from main import app
client = TestClient(app)

def test_root_ping():
    response = client.get("/")
    assert response.status_code == 200
