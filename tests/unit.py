from urlshortener import to_base62, generate_id, URLShortener
from inmemoryurlrepo import InMemoryURLRepo

def test_simple_conversion():
  assert to_base62(10) == "a"

def test_more_complex_conversion():
  assert to_base62(11157) == "2TX"

def test_larger_id_conversion():
  assert to_base62(2009215674938) == "zn9edcu"

def test_uuid_generator():
  assert isinstance(generate_id(), int)

def test_shortener_usecase_for_new_url():
  repo = InMemoryURLRepo()
  usecase = URLShortener(repo)
  longUrl = "https://en.wikipedia.org/wiki/Systems_design"
  hash = usecase.perform(longUrl)
  if not hash: assert False
  records = repo.list()
  fetchedLongUrl = records[0]["longUrl"]
  assert len(records) == 1
  assert fetchedLongUrl == longUrl

def test_shortener_usecase_for_existing_url():
  repo = InMemoryURLRepo()
  usecase = URLShortener(repo)
  longUrl = "https://en.wikipedia.org/wiki/Systems_design"
  usecase.perform(longUrl)
  usecase.perform(longUrl)
  records = repo.list()
  fetchedLongUrl = records[0]["longUrl"]
  assert len(records) == 1
  assert fetchedLongUrl == longUrl