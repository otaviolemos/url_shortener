from urlshortener import generate_id, to_base62

def test_postgres_adapter():
  repo = PostgresURLRepo()
  id = generate_id()
  longUrl = "https://en.wikipedia.org/wiki/Systems_design"
  hash = to_base62(id)
  repo.add(id, longUrl, hash)
  assert len(repo.list()) == 1
  assert repo.findByLongUrl() == hash
  assert repo.getLongUrl(id) == longUrl