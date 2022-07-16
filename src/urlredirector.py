class URLRedirector:
  def __init__(self, repo) -> None:
    self.repo = repo

  def perform(self, hash):
    key = from_base62(hash)
    longUrl = self.repo.getLongUrl(key)
    if longUrl: return longUrl
    raise Exception("Invalid hash.")

def from_base62(hash):
  base62chars = list(str(n) for n in range(10))
  base62chars = base62chars + list(chr(n) for n in range(ord('a'), ord('z')+1))
  base62chars = base62chars + list(chr(n) for n in range(ord('A'), ord('Z')+1))
  length = len(hash)
  key = 0
  for i in range(0, length):
    char = hash[length-1-i]
    if not(char.isalpha() or char.isdigit()):
      return -1
    num = base62chars.index(char)
    key += num * (62 ** i)
  return key
