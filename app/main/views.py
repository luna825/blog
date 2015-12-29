# -*- coding: UTF-8 -*-
from flask import render_template,request,current_app
from . import main
from ..models import Post

@main.route('/')
def index():
    page = request.args.get('page',1,int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page,per_page=current_app.config['FLASK_POSTS_PER_PAGE'],error_out=False)
    posts = pagination.items
    return render_template('index.html',posts=posts,digest=True,pagination=pagination)

@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html',posts=[post])

@main.route('/post/<title>')
def post_about(title):
    post = Post.query.filter_by(title=title).first()
    return render_template('post.html',posts=[post])