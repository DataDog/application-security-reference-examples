from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, current_app, g
from flask_login import login_required, current_user
from .models import Blog
from . import db
import json
import requests


blog = Blueprint('blog', __name__)


@blog.route('/', methods=['GET'])
@login_required
def home():
    return render_template("blog.html", user=current_user)

@blog.route('/add-blog', methods=['GET', 'POST'])
@login_required
def add_blog():
    print("current user", current_user.blogs)
    if request.method == 'POST': 
        blog = request.form.get('blog')
        picture_url = request.form.get('picture')

        new_blog = Blog(data=blog, user_id=current_user.id, picture_url=picture_url)  
        db.session.add(new_blog) 
        db.session.commit()
        flash('Blog added!', category='success')
        return redirect(url_for('blog.home'))

    return render_template("blog_form.html", user=current_user)

@blog.route('/flag', methods=['GET'])
@login_required
def flag():
    return render_template("flag.html", user=current_user)

@blog.route('/test_picture_url', methods=['POST'])
def test_picture_url():

    user_url = request.json.get('url')
    logger = current_app.logger
    logger.info(f"Testing user URL: {user_url}")
    try:
        response = requests.get(user_url)
        if response.status_code == 200:
            return jsonify({"success": "We are able to reach your picture"}), 200
        else:
            return jsonify({"error": f"Unable to access the URL. HTTP Status Code: {response.status_code}"}), 401
    except requests.RequestException:
        return jsonify({"error": "We can't reach this URL, please try again"}), 400
    

@blog.route('/delete-blog', methods=['POST'])
def delete_blog():  
    blog = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    blogId = blog['blogId']
    blog = blog.query.get(blogId)
    if blog:
        if blog.user_id == current_user.id:
            db.session.delete(blog)
            db.session.commit()

    return jsonify({})