from urlrepo import URLRepo

class PostgresURLRepo(URLRepo):
  def __init__(self, conn) -> None:
    super().__init__()
    self.conn = conn

  def add(self, id, longUrl, hash):
    cur = self.conn.cursor()
    cur.execute('INSERT INTO url (id, longUrl, hash) VALUES'
                '(%s, %s, %s);', (id, longUrl, hash))
    self.conn.commit()
    cur.close()

  def list(self):
    cur = self.conn.cursor()
    cur.execute("SELECT * FROM url;")
    return cur.fetchall()

  def findByLongUrl(self, longUrl):
    cur = self.conn.cursor()
    cur.execute('SELECT hash FROM url WHERE longUrl = %s', (longUrl,))
    fetched = cur.fetchone()
    if fetched:
      return fetched[0]
    return None

  def getLongUrl(self, key):
    cur = self.conn.cursor()
    cur.execute('SELECT longUrl FROM url WHERE id = %s', (key,))
    fetched = cur.fetchone()
    if fetched:
      return fetched[0]
    return None