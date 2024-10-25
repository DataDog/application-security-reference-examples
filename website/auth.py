from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for
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
        return render_template("index.html")
    else:
        new_user = User(username="username", password=generate_password_hash("password"))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        return redirect(url_for('auth.home'))  
    return render_template("index.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                print(username, password, "success!")
                print(user.id)
                login_user(user)
                # This is needed for the datadog tracer to get the user id for credential stuffing attacks
                # set_user(tracer, user.id, name=user.username, propagate=True)
                track_user_login_success_event(tracer, user.id)
                print(user.get_id())
                return redirect(url_for('views.home_page')), 200
            else:
                # set_user(tracer, user.id, name=user.username, propagate=True)
                exists = True
                track_user_login_failure_event(tracer, user.id, exists)
                print("wrong email or password")
                flash('wrong email or password.', category='error')
                return render_template("login.html"), 401
        else:
            # set_user(tracer, None, username, propagate=True)
            exists = False
            track_user_login_failure_event(tracer, None, exists)
            print("wrong email or password")
            flash('wrong email or password.', category='error')
            return render_template("login.html"), 401
    return render_template("login.html", user=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)
        user = User.query.filter_by(username=username).first()
        
        if user:
            flash('Email already exists.', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('auth.home')), 200

    return render_template("register.html", user=current_user)