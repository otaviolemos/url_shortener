from postgresurlrepo import PostgresURLRepo
from urlshortener import generate_id, to_base62
import psycopg2

def test_postgres_adapter():
  host='localhost'
  database='url_shortener'
  user='test_user'
  password='1234'
  conn = get_db_connection(host, database, user, password)
  clear_db(conn)
  repo = PostgresURLRepo(conn)
  id = generate_id()
  longUrl = "https://en.wikipedia.org/wiki/Systems_design"
  hash = to_base62(id)
  repo.add(id, longUrl, hash)
  assert len(repo.list()) == 1
  assert repo.findByLongUrl(longUrl) == hash
  assert repo.getLongUrl(id) == longUrl
  clear_db(conn)
  close_connection(conn)

def get_db_connection(host, database, user, password):
  conn = psycopg2.connect(host=host, database=database, user=user, password=password)
  return conn

def close_connection(conn):
  conn.close()

def clear_db(conn):
  cur = conn.cursor()
  cur.execute('DELETE FROM url;')
  conn.commit()