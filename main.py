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
    return render_template("about.html")

@app.route("/register")
def register():
    return render_template("register.html")



if __name__ == "__main__":
    app.run(debug=True)
