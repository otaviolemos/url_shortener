from flask import Flask, request, jsonify
from factories import make_repo, make_shorten_usecase

def create_app():
  app = Flask(__name__)
  repo = make_repo()
  @app.route("/shorten", methods = ['POST'])
  def shorten():
    longUrl = request.json["longUrl"]
    shorten_usecase = make_shorten_usecase(repo)
    result = { "hash": shorten_usecase.perform(longUrl) }
    return jsonify(result), 200
  return app

app = create_app()