import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_shortening_url(client):
  longUrl = "https://en.wikipedia.org/wiki/Systems_design"
  response = client.post("/shorten", json={"longUrl": longUrl})
  assert response.status_code == 201
  assert response.json["hash"] is not None
