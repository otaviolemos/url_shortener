from urlredirector import URLRedirector
from urlshortener import URLShortener
from inmemoryurlrepo import InMemoryURLRepo

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

def test_redirector_use_case():
  originalLongUrl = "https://en.wikipedia.org/wiki/Systems_design"
  hash = "zn9edcu"
  repo = InMemoryURLRepo()
  repo.add(2009215674938, originalLongUrl, hash)
  usecase = URLRedirector(repo)
  fetchedLongUrl = usecase.perform(hash)
  assert fetchedLongUrl == originalLongUrl