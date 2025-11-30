# -*- coding: utf-8 -*-

"""
@Time   :2025/11/23 12:52
@Author : dongwenhao 
@File   : app_schema.py
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CompletionForm(FlaskForm):
    user_query = StringField("user_query", validators=[
        DataRequired(message="用户的问题必填"),
        Length(min=1, max=2000, message="用户提问内容最大长度是2000")
    ])

class TestForm(FlaskForm):
    name = StringField("name", validators=[
        DataRequired(message="名称是必填项"),
        Length(min=1, max=32, message="用户名称最长32个字符")
    ])
    status = StringField("status", validators=[
        DataRequired(message="名称是必填项"),
    ])

