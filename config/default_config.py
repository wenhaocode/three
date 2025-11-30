# -*- coding: utf-8 -*-

"""
@Time   :2025/11/25 12:57
@Author : dongwenhao 
@File   : default_config.py
"""

"""应用的默认配置"""

# Flask默认配置
FLASK_DEFAULT_CONFIG = {
    "WTF_CSRF_ENABLED": False,
}

# SQLAlchemy数据库默认配置
SQLALCHEMY_DEFAULT_CONFIG = {
    "DB_SERVER": "mysql",
    "USERNAME": "root",
    "PASSWORD": "",
    "HOST": "127.0.0.1",
    "PORT": "5432",
    "DATABASE": "postgres",
    "ENCODING": "utf-8",
    "POOL_SIZE": 30,
    "POOL_RECYCLE": 3600,
    "ECHO": "True",
}