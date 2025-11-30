# -*- coding: utf-8 -*-

"""
@Time   :2025/11/20 14:34
@Author : dongwenhao 
@File   : $NAME.py
"""
# 引入当前路径下的文件和对应的类
from .app_handler import AppHandler

# 通过__all__魔术变量,将上面的AppHandler类导出
__all__ = ["AppHandler"]
