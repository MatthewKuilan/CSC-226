from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from extensions import db
from models import User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/matthew/Documents/GitHub/CSC-226/instance/house_sorter.db"
db.init_app(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template('user/list.html', users=users)

#user=User{} is for creating a new user instance not updating one, later I used wallet_choice=wallet_choice because of this
@app.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        print(request.form)
        user = User(
            username=request.form["username"],
            email=request.form["email"],
            choice=request.form["choice"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))
    
    return render_template("user/create.html")

@app.route("/user/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template("user/detail.html", user=user)


# user=user passes the entire user object, id=user.id only passes the id
@app.route("/quiz/<int:id>")
def user_quiz(id):
    user = db.get_or_404(User, id)
    return render_template("user/quiz.html", id=user.id)

# Can't think of a reason why I'm getting id from form and not just explicitly passing it. 
@app.route("/save_quiz/<int:id>", methods=["POST"])
def save_user_quiz(id):    
    try:
        #getting form data then updating user
        wallet_choice=request.form.get("wallet_choice")
        bully_choice=request.form.get("bully_choice")
        challenge_choice=request.form.get("challenge_choice")
        game_choice=request.form.get("game_choice")
        motivation_choice=request.form.get("motivation_choice")
        house=request.form.get("house_name")
        
        if id:
            user = db.get_or_404(User, id)
            user.wallet_choice=wallet_choice
            user.bully_choice=bully_choice
            user.challenge_choice=challenge_choice
            user.game_choice=game_choice
            user.motivation_choice=motivation_choice
            user.house=house

            db.session.commit()
            return jsonify({
                'success': True,
                'Message': 'Quiz results saved for existing user!',
                'redirect_url': url_for("user_detail", id=user.id)
            })
    except Exception as e:
        return jsonify({'Success': False, 'Error': str(e)})
        
@app.route("/houses", methods=["GET"])
def houses():
    users_with_houses = db.session.execute(
        db.select(User).where(User.house != None).order_by(User.house, User.username)
    ).scalars()
    
    houses_dict = {
        "Gryffindor": [],
        "Hufflepuff": [],
        "Ravenclaw": [],
        "Slytherin": []
    }
    
    for user in users_with_houses:
        if user.house in houses_dict:
            houses_dict[user.house].append(user)
    
    return render_template('houses.html', houses=houses_dict)

@app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(User, id)

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("user_list"))
    
    return render_template("user/delete.html", user=user)

if __name__ == '__main__':
    with app.app_context():
        print("are we reaching this?")
        db.create_all()
    app.run(debug=True)