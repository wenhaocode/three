# -*- coding: utf-8 -*-

"""
@Time   :2025/11/25 18:37
@Author : dongwenhao 
@File   : test_model.py
"""

from internal.extension.database_extension import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Table

class TestModel(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="自增主键")
    name = db.Column(db.String(32), nullable=False, comment="名称")
    status = db.Column(db.String(16), nullable=False, comment="状态")