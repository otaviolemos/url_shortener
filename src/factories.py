from inmemoryurlrepo import InMemoryURLRepo
from postgresurlrepo import PostgresURLRepo
from urlredirector import URLRedirector
from urlshortener import URLShortener
from flask import g

def make_repo():
  return PostgresURLRepo(g.db)

def make_shorten_usecase(repo):
  return URLShortener(repo)

def make_redirector_usecase(repo):
  return URLRedirector(repo)