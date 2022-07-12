from flask import Flask, request, jsonify, make_response, g
from factories import make_repo, make_shorten_usecase, make_redirector_usecase
import psycopg2

def create_app():
  app = Flask(__name__)

  @app.before_request
  def before_request():
    host='localhost'
    database='url_shortener'
    user='test_user'
    password='1234'
    conn = get_db_connection(host, database, user, password)
    g.db = conn

  @app.route("/shorten", methods = ['POST'])
  def shorten():
    longUrl = request.json["longUrl"]
    repo = make_repo()
    shorten_usecase = make_shorten_usecase(repo)
    result = { "hash": shorten_usecase.perform(longUrl) }
    return jsonify(result), 200
  
  @app.route("/<hash>", methods = ['GET'])
  def redirect(hash):
    repo = make_repo()
    redirector_usecase = make_redirector_usecase(repo)
    try:
      longUrl = redirector_usecase.perform(hash)
      response = make_response()
      response.headers['location'] = longUrl
      response.status_code = 301
      return response
    except:
      return "Invalid hash.", 404
  
  @app.after_request
  def after_request(response):
    if g.db is not None:
      g.db.close()
    return response
  return app


def get_db_connection(host, database, user, password):
  conn = psycopg2.connect(host=host, database=database, user=user, password=password)
  return conn

app = create_app()