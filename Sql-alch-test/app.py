from flask import Flask, render_template, request, redirect, url_for
from extensions import db
from models import User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db.init_app(app)

from models import User

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template('user/list.html')

@app.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
            radio=request.form["choice"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))
    
    return render_template("user/create.html")

@app.route("/user/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template("user/detail.html", user=user)

@app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(user, id)

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("user_list"))
    
    return render_template("/index.html")
    # return render_template(user/delete.html, user=user)

with app.app_context():
    db.create_all()