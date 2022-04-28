from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def read():
    users=User.get_all()
    return render_template('read.html', all_users = users)

@app.route("/users/form")
def forms():
    return render_template('create.html')

@app.route("/users/new", methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)
