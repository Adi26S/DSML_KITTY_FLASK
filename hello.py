from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>This will trigger me!!!!</p>"


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def main_page():
    return "</H1>WELCOME TO MY WEBSITE MF'SSSSSS!!!!</H1>"