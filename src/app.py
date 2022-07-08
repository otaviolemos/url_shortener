from flask import Flask, request, jsonify, make_response
from factories import make_repo, make_shorten_usecase, make_redirector_usecase

def create_app():
  app = Flask(__name__)
  repo = make_repo()

  @app.route("/shorten", methods = ['POST'])
  def shorten():
    longUrl = request.json["longUrl"]
    shorten_usecase = make_shorten_usecase(repo)
    result = { "hash": shorten_usecase.perform(longUrl) }
    return jsonify(result), 200
  
  @app.route("/<hash>", methods = ['GET'])
  def redirect(hash):
    redirector_usecase = make_redirector_usecase(repo)
    try:
      longUrl = redirector_usecase.perform(hash)
      response = make_response()
      response.headers['location'] = longUrl
      response.status_code = 301
      return response
    except:
      return "Invalid hash.", 404
  return app

app = create_app()