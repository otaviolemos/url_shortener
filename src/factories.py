from inmemoryurlrepo import InMemoryURLRepo
from urlredirector import URLRedirector
from urlshortener import URLShortener

def make_repo():
  return InMemoryURLRepo()

def make_shorten_usecase(repo):
  return URLShortener(repo)

def make_redirector_usecase(repo):
  return URLRedirector(repo)