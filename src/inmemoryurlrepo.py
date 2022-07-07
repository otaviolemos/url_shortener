from urlrepo import URLRepo

class InMemoryURLRepo(URLRepo):
  def __init__(self) -> None:
    super().__init__()
    self.records = {}

  def add(self, id, longUrl, hash):
    self.records[id] = {"hash": hash, "longUrl": longUrl}

  def list(self):
    return list(self.records.values())
  
  def findByLongUrl(self, longUrl):
    values = list(self.records.values())
    for value in values:
      if value["longUrl"] == longUrl:
        return value["hash"]
    return None

  def getLongUrl(self, key):
    return (self.records[key])["longUrl"]