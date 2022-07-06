from core import generate_id, to_base62

class URLShortener:
  def __init__(self, repo) -> None:
    self.repo = repo
  
  def perform(self, longUrl):
    id = generate_id()
    hash = to_base62(id)
    self.repo.add(id, longUrl, hash)