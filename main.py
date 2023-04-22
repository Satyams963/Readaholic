from flask import Flask, render_template
from forms import AdminRegistrationForm 
from forms import AdminLoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config[ 'SECRET_KEY'] = 'secret_key_33'
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), nullable = False)
    password = db.Column(db.String(32), nullable = False)

    def __repr__(self):
        return f"User(email: {self.email})"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), nullable = False)
    author = db.Column(db.String(60))
    isbn = db.Column(db.Integer, unique = True, nullable = False)
    genre = db.Column(db.String(60), nullable = False)
    shop_link = db.Column(db.String(60), nullable = True)
    rating = db.Column(db.Float(32), nullable = False)
    image = db.Column(db.String(32), default = "default.jpg")
    tiny_summary = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f"Book(title: {self.title}, isbn: {self.isbn})"




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

@app.route("/register", methods=["GET", "POST"])
def register():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        _email = form.data['email']
        _password = form.data['password']
        user = User(email = _email, password = _password)
        db.session.add(user)
        db.session.commit()
        print("User added")
    return render_template("register.html", form = form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template("login.html", form = form)

@app.route("/books")
def books():
    return render_template("books.html")



if __name__ == "__main__":
    app.run(debug=True)
