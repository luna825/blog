# -*- coding: UTF-8 -*-
from . import db,login_manager
from flask.ext.login import UserMixin,AnonymousUserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from markdown import markdown
import bleach

class Administor(db.Model,UserMixin):
	__tablename__ = 'administors'
	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(64),unique=True,index=True)
	password_hash = db.Column(db.String(128))
	name = db.Column(db.String(64))
	location = db.Column(db.String(64))
	about_me = db.Column(db.Text())
	posts = db.relationship('Post',backref='author',lazy='dynamic')

	@property
	def password(self):
		raise AttributeError('不能读取密码！')
	@password.setter
	def password(self,password):
		self.password_hash = generate_password_hash(password)
	def verify_password(self,password):
		return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
	return Administor.query.get(int(user_id))

class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(128),index=True)
	body = db.Column(db.Text)
	body_html = db.Column(db.Text)
	timestamp = db.Column(db.DateTime,index = True,default=datetime.utcnow)
	author_id = db.Column(db.Integer,db.ForeignKey('administors.id'))

	@staticmethod
	def on_changed_body(target,value,oldvalue,initiator):
		allowed_tags=['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
		target.body_html = bleach.linkify(bleach.clean(
        	markdown(value,output_format='html'),tags=allowed_tags,strip=True))
		
db.event.listen(Post.body,'set',Post.on_changed_body)


