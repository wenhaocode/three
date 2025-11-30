# -*- coding: utf-8 -*-

"""
@Time   :2025/11/20 17:58
@Author : dongwenhao 
@File   : app.py
"""

# 引入server包下自定义的Http类
from internal.server.http import Http
from internal.extension import db

# 引入injector
from injector import Injector
# 创建injector实体类
injector = Injector()

# 引入dotenv
from dotenv import load_dotenv
load_dotenv()

# 引入自定义的Config类, 并实例化
from config import Config
config = Config()

# 引入Router类, 通过injector实例化对象实现路由注入
from internal.router import Router
app = Http(__name__, config=config, db=db, router=injector.get(Router))

# 运行当前flask服务
if __name__ == '__main__':
    app.run(debug=True)