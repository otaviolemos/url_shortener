from core import to_base62
from core import generate_id
from urlshortener import URLShortener
from inmemoryurlrepo import InMemoryURLRepo


def test_simple_conversion():
  assert to_base62(10) == "a"

def test_more_complex_conversion():
  assert to_base62(11157) == "2TX"

def test_larger_id_conversion():
  assert to_base62(2009215674938) == "zn9edcu"

def test_uuid_generator():
  assert isinstance(generate_id(), int)

def test_shortener_operation():
  repo = InMemoryURLRepo()
  usecase = URLShortener(repo)
  usecase.perform("https://en.wikipedia.org/wiki/Systems_design")
  if "hash" in repo.get("https://en.wikipedia.org/wiki/Systems_design"):
    assert True
  else: assert False