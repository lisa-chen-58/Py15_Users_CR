from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

# Home Route


@app.route("/")
def index():
    return redirect("/users")


@app.route('/users')
def users():
    return render_template('all_users.html', users=User.get_all())


@app.route('/users/new')
def new_user():
    return render_template('create.html')


@app.route('/create/user', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.save(data)
    return redirect('/users')
