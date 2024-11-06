from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from ddtrace.contrib.trace_utils import set_user
from ddtrace.appsec.trace_utils import track_user_login_failure_event, track_user_login_success_event
from ddtrace import tracer


auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def home():
    user = User.query.filter_by(username="username").first()
    if user:
        return render_template("home.html")
    else:
        new_user = User(username="username", password=generate_password_hash("password"))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        return render_template("login.html") 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                # needed to track business logic with the datadog tracer
                track_user_login_success_event(tracer, user.id)
                return render_template("home.html"), 200
            else:
                # needed to track business logic with the datadog tracer
                exists = True
                track_user_login_failure_event(tracer, user.id, exists)
                print("wrong email or password")
                flash('wrong email or password.', category='error')
                return render_template("login.html"), 401
        else:
            # needed to track business logic with the datadog tracer
            exists = False
            track_user_login_failure_event(tracer, str(username), exists)
            print("wrong email or password")
            flash('wrong email or password.', category='error')
            return render_template("login.html"), 401
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("login.html")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user:
            flash('Email already exists.', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return render_template("home.html"), 200

    return render_template("register.html", user=current_user)