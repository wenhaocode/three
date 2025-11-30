# -*- coding: utf-8 -*-

"""
@Time   :2025/11/20 16:46
@Author : dongwenhao 
@File   : router.py
"""

# 引入flask框架工具和蓝图工具
from flask import Flask, Blueprint
# 引入自定义的控制器对象
from internal.handler import AppHandler

# 引入inject依赖注入工具, 为Router路由类注入所需的Handler控制器对象
from injector import inject
# 引入dataclass, 用于对注入的handler类进行自动的init初始化绑定和赋值
from dataclasses import dataclass
# 定义路由类,并使用inject装饰 和 dataclass装饰
@inject
@dataclass
class Router:
    """
    由于我们使用inject依赖注入装饰,
    因此AppHandler自定义控制器类需要在当前Router类的init初始化方法中进行赋值
    但由于我们又引入了dataclass装饰,
    因此, 所有需要依赖注入的类, dataclass都会自动帮我们实现init初始化赋值
    因此, Router类中的__init__初始化方法不需要我们手动去定义了.
    """

    # def __init__(self, app_handler: AppHandler):
    #     self.app_handler = app_handler

    # 定义路由注册函数
    def register_router(self, app: Flask):
        """注册路由"""
        # 创建蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 将url与对应的控制器方法做绑定
        app_handler = AppHandler()

        # 绑定一个路由和对应的函数
        bp.add_url_rule("/ping", view_func=app_handler.ping, methods=["GET"])
        bp.add_url_rule("/completion", view_func=app_handler.completion, methods=["POST"])
        bp.add_url_rule("/test_add_info", view_func=app_handler.test_add_info, methods=["POST"])

        # 在应用上注册蓝图
        app.register_blueprint(bp)
