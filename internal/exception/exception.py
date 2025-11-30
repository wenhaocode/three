# -*- coding: utf-8 -*-

"""
@Time   :2025/11/24 10:10
@Author : dongwenhao 
@File   : exception.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode

# 自定义基础异常信息类, 继承python的Exception
class CustomException(Exception):
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        # 调用父类初始化函数
        super().__init__(message)
        self.message = message
        self.data = data

# 通用的失败异常类
class FailedException(CustomException):
    pass

# 未找到异常
class NotFoundException(CustomException):
    code = HttpCode.NOT_FOUND

# 未授权异常
class UnauthorizedException(CustomException):
    code = HttpCode.UNAUTHORIZED

# 无权限异常
class ForbiddenException(CustomException):
    code = HttpCode.FORBIDDEN

# 参数校验异常
class ValidateErrorException(CustomException):
    code = HttpCode.VALIDATE_ERROR
