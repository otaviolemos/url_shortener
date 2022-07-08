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
  response = client.post("/api/shorten", data=dict(
      longUrl="https://en.wikipedia.org/wiki/Systems_design"
    ))
  assert response.data == b"Hello, World!"
