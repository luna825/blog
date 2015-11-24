# -*- coding: UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import Administor
from flask.ext.pagedown.fields import PageDownField

class LoginForm(Form):
	email = StringField('邮 箱',validators=[Required(),Email(),Length(1,64)])
	password = PasswordField('密 码',validators=[Required()])
	remember_me = BooleanField('记住我')
	submit = SubmitField('登 录')

class PostForm(Form):
	title = StringField('',validators=[Required()])
	body = PageDownField('',validators=[Required()])
	submit = SubmitField('发布文章')
