# -*- coding: utf-8 -*-

"""
@Time   :2025/11/25 18:41
@Author : dongwenhao 
@File   : app_service.py
"""

from flask_sqlalchemy import SQLAlchemy

# 引入dataclass, 修饰当前类
from dataclasses import dataclass
# 引入inject装饰器, 采用注入方式
from injector import inject

from internal.model.test_model import TestModel

@inject
@dataclass
class AppService:
    # 在AppService类中声明一个db属性, 属性类型为SQLAlchemy
    db: SQLAlchemy

    def create_test(self, insert_data: dict):
        # 1. 创建模型的实体类
        test_model = TestModel()

        # 2. 赋值
        test_model.name = insert_data.get('name')
        test_model.status = insert_data.get('status')
        # 3. 将实体类添加到Session会话中
        self.db.session.add(test_model)
        # 4. 提交Session会话
        self.db.session.commit()