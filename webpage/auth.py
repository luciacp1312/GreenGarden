from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .database import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db

# Using Blueprint, we don't need to have all the views in one file, we can split them in multiple files
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # GET and POST are requests sent to our server
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')

        user = User.query.filter_by(email=email).first() # This is to return the first result of the query
        if user:
            if check_password_hash(user.password, password): # decrypt the password and checks it
                flash('Logged in successfully', category='success')
                login_user(user, remember=True) # remember is used to stay logged until you logout of the page, even though you close the window
                return redirect(url_for('views.home'))
            else:
                flash('The password is incorrect', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user) # From flask_login It contains info about the user. In case we are currently logged, it will redirect us to the home page

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')

        user = User.query.filter_by(email=email).first()
        if user:
            # flash is a type of message in flask that will be shown at the top of the screen. Right bellow the navbar
            flash('The email already exists', category='error')
        elif len(email) < 4:
            flash('The email must be greater than 3 characters', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character', category='error')
        elif pass1 != pass2:
            flash('The passwords don\'t match', category='error')
        elif len(pass1) < 5:
            flash('Password must be at least 5 characters', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(pass1, method='sha256')) # hash is a way to secure a password encrypting it. sha256 is a hashing algorithm
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Your account has been successfully created', category='success')
            return redirect(url_for('views.home')) # To redirect the user to the main page

    return render_template("sign_up.html", user=current_user)
