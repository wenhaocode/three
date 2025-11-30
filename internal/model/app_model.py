# -*- coding: utf-8 -*-

"""
@Time   :2025/11/25 18:59
@Author : dongwenhao 
@File   : app_model.py
"""
from internal.extension.database_extension import db

class App(db.Model):
    __tablename__ = 'app'