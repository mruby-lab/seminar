from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello() -> str:
    return "Web server is working."

@app.route("/hello")
def home() -> str:
    return "Hello"

if __name__ == "__main__":
    app.run()