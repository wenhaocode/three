# -*- coding: utf-8 -*-

"""
@Time   :2025/11/23 21:12
@Author : dongwenhao 
@File   : http_code.py
"""

from enum import Enum

class HttpCode(str, Enum):
    """HTTP基础业务状态码"""
    SUCCESS = "success"                     # 请求成功
    FAIL = "fail"                           # 请求失败
    NOT_FOUND = "not_found"                 # 未找到
    UNAUTHORIZED = "unauthorized"           # 未登录
    FORBIDDEN = "forbidden"                 # 无权限
    VALIDATE_ERROR = "validation_error"     # 数据验证错误