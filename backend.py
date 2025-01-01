# type: ignore
from flask import Flask, render_template, request, jsonify
from pyngrok import ngrok
from dotenv import load_dotenv, dotenv_values

load_dotenv()
env_vars = dotenv_values()

ngrok.set_auth_token(env_vars["NGROK_AUTH_TOKEN"])
public_url = ngrok.connect(env_vars["PORT"])

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
  return jsonify({"message": "Hello, World!"}), 200

@app.route("/get-prompt", methods=["GET"])
def get_prompt():
  if request.method == "GET":
    question = request.args.get("question")
    response = query_engine.query(question)
    return jsonify(response), 200
  else:
    question = request.args.get("question")
    return jsonify({"Error": "Invalid request method."}), jsonify(response), 500

@app.route("/post-prompt", methods=["POST"])
def post_prompt():
  if request.method == "POST":
    question = request.form.get("question")
    response = query_engine.query(question)
    return jsonify(response), jsonify(question), 200
  else:
    question = request.form.get("question")
    return jsonify({"Error": "Invalid request method."}), jsonify(question), 500

if __name__ == '__main__':
  print(public_url)
  app.run(port=int(env_vars["PORT"]), debug=False)
