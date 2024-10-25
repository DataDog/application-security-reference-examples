from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
def home_page():
    print(User.get_id(current_user))
    return render_template("home.html", user=current_user)