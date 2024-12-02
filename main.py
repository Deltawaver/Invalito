from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index.html")
def back():
    return render_template("index.html")


@app.route("/single.html")
def item():
    return render_template("single.html")


if __name__ == "__main__":
    app.run(debug=True)
