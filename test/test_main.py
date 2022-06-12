from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


fpath = "test_images/dog.1.jpg"


def test_predict():
    with open(fpath, "rb") as f:
        files = {'image': f}

        response = client.post("/predict", files=files)
        assert response.status_code == 202
        assert response.json() == {'ANIMAL': 'Its a Dog'}




