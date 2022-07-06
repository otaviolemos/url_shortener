from urlrepo import URLRepo

class InMemoryURLRepo(URLRepo):
  def __init__(self) -> None:
    super().__init__()
    self.records = {}

  def add(self, id, longUrl, hash):
    self.records[longUrl] = {"hash": hash, "id": id}

  def get(self, longUrl):
    return self.records[longUrl]