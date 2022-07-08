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
  assert response.status_code == 200
  assert response.json["hash"] is not None

def test_redirect(client):
  longUrl = "https://en.wikipedia.org/wiki/Systems_design"
  post_response = client.post("/shorten", json={"longUrl": longUrl})
  hash = str(post_response.json["hash"])
  get_parameter = "/" + hash
  get_response = client.get(get_parameter)
  assert get_response.status_code == 301
  assert get_response.headers["location"] == longUrl



