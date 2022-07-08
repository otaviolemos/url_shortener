from inmemoryurlrepo import InMemoryURLRepo
from urlshortener import URLShortener

def make_repo():
  return InMemoryURLRepo()

def make_shorten_usecase(repo):
  return URLShortener(repo)