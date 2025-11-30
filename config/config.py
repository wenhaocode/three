# -*- coding: utf-8 -*-

"""
@Time   :2025/11/23 14:31
@Author : dongwenhao 
@File   : config.py
"""
import os
from typing import Any
# 引入自定义的默认配置参数
from .default_config import SQLALCHEMY_DEFAULT_CONFIG, FLASK_DEFAULT_CONFIG


class Config:
    def __init__(self):
        # 关闭wtf的csrf保护
        self.WTF_CSRF_ENABLED = os.getenv("WTF_CSRF_ENABLED", FLASK_DEFAULT_CONFIG.get("WTF_CSRF_ENABLED"))

        # 获取环境变量中的配置信息
        db_server = os.getenv("DB_SERVER", SQLALCHEMY_DEFAULT_CONFIG.get("DB_SERVER"))
        host = os.getenv("HOST", SQLALCHEMY_DEFAULT_CONFIG.get("HOST"))
        port = os.getenv("PORT", SQLALCHEMY_DEFAULT_CONFIG.get("PORT"))
        username = os.getenv("USERNAME", SQLALCHEMY_DEFAULT_CONFIG.get("USERNAME"))
        password = os.getenv("PASSWORD", SQLALCHEMY_DEFAULT_CONFIG.get("PASSWORD"))
        database = os.getenv("DATABASE", SQLALCHEMY_DEFAULT_CONFIG.get("DATABASE"))
        encoding = os.getenv("ENCODING", SQLALCHEMY_DEFAULT_CONFIG.get("ENCODING"))
        pool_size = int(os.getenv("POOL_SIZE", SQLALCHEMY_DEFAULT_CONFIG.get("POOL_SIZE")))
        pool_recycle = int(os.getenv("POOL_RECYCLE", SQLALCHEMY_DEFAULT_CONFIG.get("POOL_RECYCLE")))
        echo = os.getenv("ECHO", SQLALCHEMY_DEFAULT_CONFIG.get("ECHO"))

        # 拼接出数据库配置, 并将配置参数绑定在config类上
        self.SQLALCHEMY_DATABASE_URI = f"{db_server}://{username}:{password}@{host}:{port}/{database}?client_encoding={encoding}"
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": pool_size,
            "pool_recycle": pool_recycle,
        }
        self.SQLALCHEMY_ECHO = echo
