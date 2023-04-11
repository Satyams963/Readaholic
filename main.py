from flask import Flask, render_template

app = Flask(__name__)

title = "Readaholic"
data = {
    "website_name": "Readaholic",
    "author": "Satyam"
    }

@app.route("/")
def home():
    return render_template("home.html", data = data)

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# @app.route("/route1")
# @app.route("/route2")
# @app.route("/route3")
# def route1():
#     return "<h1>Hello, Satyam</h1>"


if __name__ == "__main__":
    app.run(debug=True)
