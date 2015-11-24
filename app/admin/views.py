# -*- coding: UTF-8 -*-
from flask import render_template,url_for,flash,redirect,request
from flask.ext.login import login_user,login_required,logout_user,current_user
from . import admin
from forms import LoginForm,PostForm
from ..models import Administor,Post
from .. import db

@admin.route('/login',methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		administor = Administor.query.filter_by(email=form.email.data).first()
		if administor and administor.verify_password(form.password.data):
			login_user(administor,form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index'))
		flash('用户名或密码错误')
	return render_template('admin/login.html',form = form)

@admin.route('/post',methods=["GET","POST"])
@login_required
def post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data,
			body = form.body.data,
			author = current_user._get_current_object())
		db.session.add(post)
		return redirect(url_for('main.index'))
	return render_template('admin/post.html',form=form)