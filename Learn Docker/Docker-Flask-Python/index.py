from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\":\"Hey there PYTHON\"}"

if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("3030"), debug=True)