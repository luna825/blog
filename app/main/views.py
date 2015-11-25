# -*- coding: UTF-8 -*-
from flask import render_template
from . import main
from ..models import Post

@main.route('/')
def index():
	posts = Post.query.order_by(Post.timestamp.desc()).all()
	return render_template('index.html',posts=posts,digest=True)

@main.route('/post/<int:id>')
def post(id):
	post = Post.query.get_or_404(id)
	return render_template('post.html',posts=[post])

@main.route('/post/<title>')
def post_about(title):
	post = Post.query.filter_by(title=title).first()
	return render_template('post.html',posts=[post])