from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
auth = Blueprint("auth", __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect Password!", category="error")
        else:
            flash("Account doesn't exists. Please Sign Up!", category="error")
    return render_template("login.html", user=current_user)


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash("Email Already Exists. Please Login", category="error")
        elif username_exists:
            flash("Username Already Exists.", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        elif len(email) < 10:
            flash("Email too short!", category="error")
        elif len(username) < 2:
            flash("Username too short!", category="error")
        elif len(password1) < 8:
            flash("Password too short!", category="error")
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash(f"Account created! Welcome {username}")
            # this needs to be changed upon the syntax by arjun and arsh
            return redirect(url_for("views.home"))
    return render_template("sign_up.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))
