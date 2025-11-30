# -*- coding: utf-8 -*-

"""
@Time   :2025/11/20 17:54
@Author : dongwenhao 
@File   : http.py
"""
import os

from flask import Flask
# 导入路由
from internal.router import Router
# 引入Config配置类
from config import Config
# 导入自定义异常
from internal.exception import CustomException
from pkg.response import HttpCode
from pkg.response.response import encode_json, Response
# 引入sql-alchemy
from flask_sqlalchemy import SQLAlchemy


class Http(Flask):
    """Http服务引擎"""

    # 定义Http类的初始化函数
    # *args代表非命名参数; **kwargs代表命名参数; router是引入的路由对象
    def __init__(self, *args, config: Config, db: SQLAlchemy, router: Router, **kwargs,):
        # 1. 使用super调用父类的构造函数
        super(Http, self).__init__(*args, **kwargs)

        # 2. 将自定义的Config加载到当前http对象中
        self.config.from_object(config)

        # 3. 注册异常处理类
        self.register_error_handler(Exception, self._register_error_handler)

        # 4. 通过传入的sql-alchemy对象, 调用init_app()函数, 初始化flask-sqlalchemy扩展
        db.init_app(self)

        # 5. 注册应用路由
        router.register_router(self)

    # 定义一个异常处理的函数
    def _register_error_handler(self, error: Exception):
        # 1. 判断异常信息是不是我们自定义的异常, 如果是, 那么可以提取message和code信息
        if isinstance(error, CustomException):
            return encode_json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data else None,
            ))
        # 2. 如果不是我们自定义的异常信息, 则有可能是框架\数据库等抛出的异常, 也可以提取信息, 设置为FAIL状态码
        if os.getenv("DEBUG"):
            # 2.1 如果是调试状态, 那么直接抛出原始异常信息
            raise error
        else:
            # 2.2 非调试状态, 返回自定义错误响应
            return encode_json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))