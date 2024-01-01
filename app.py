from flask import Flask
# module name is always lower case

app = Flask(__name__)


# everything after domain name
@app.route("/")
def hello_world():
  return "Hello World!"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
