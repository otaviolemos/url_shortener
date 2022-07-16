from uuid import uuid4

class URLShortener:
  def __init__(self, repo) -> None:
    self.repo = repo
  
  def perform(self, longUrl):
    existingHash = self.repo.findByLongUrl(longUrl)
    if existingHash:
      return existingHash
    id = generate_id()
    hash = to_base62(id)
    self.repo.add(id, longUrl, hash)
    return hash

def to_base62(num):
  base62chars = list(str(n) for n in range(10))
  base62chars = base62chars + list(chr(n) for n in range(ord('a'), ord('z')+1))
  base62chars = base62chars + list(chr(n) for n in range(ord('A'), ord('Z')+1))
  converted = ""
  while num // 62 != 0:
    remainder = num % 62
    converted += base62chars[remainder]
    num = num // 62
  converted += base62chars[num % 62]
  return converted[::-1]

def generate_id():
  return uuid4().int>>104