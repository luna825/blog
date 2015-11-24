# -*- coding: UTF-8 -*-
from flask import render_template
from . import main
from ..models import Post

@main.route('/')
def index():
	posts = Post.query.order_by(Post.timestamp.desc()).all()
	return render_template('index.html',posts=posts)

@main.route('/post/<int:id>')
def post(id):
	post = Post.query.get_or_404(id)
	return render_template('post.html',posts=[post])