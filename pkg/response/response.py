# -*- coding: utf-8 -*-

"""
@Time   :2025/11/23 21:34
@Author : dongwenhao 
@File   : response.py
"""
from pkg.response.http_code import HttpCode
from typing import Any
from dataclasses import field, dataclass
from flask import jsonify

"""基础HTTP接口响应格式"""
@dataclass
class Response:
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)

# 将一个入参jsonify之后再返回
def encode_json(data: Response = None):
    return jsonify(data), 200

# 成功的数据响应
def data_res(data: Any = None, message: str = ""):
    return encode_json(
        Response(
            code=HttpCode.SUCCESS,
            message=message,
            data=data
        )
    )

# 失败的数据响应
def fail_data_res(data: Any = None, message: str = ""):
    return encode_json(
        Response(
            code=HttpCode.FAIL,
            message=message,
            data=data
        )
    )

# 请求参数验证错误
def validate_error_res(error:dict = None):
    # 获取error消息
    error_first_key = next(iter(error))
    if error_first_key is not None:
        msg = error.get(error_first_key)[0]
    else:
        msg = ""
    return encode_json(
        Response(
            code=HttpCode.VALIDATE_ERROR,
            message=msg,
            data=error
        )
    )

# 无需返回数据, 只返回成功结果
def success_res(message: str = ""):
    return encode_json(
        Response(
            code = HttpCode.SUCCESS,
            message = message,
            data = {}
        )
    )

# 无需返回数据, 只返回失败结果
def fail_res(message: str = ""):
    return encode_json(
        Response(
            code = HttpCode.FAIL,
            message=message,
            data={}
        )
    )

# 未找到状态的消息响应
def not_found_res(message: str = ""):
    return encode_json(
        Response(
            code = HttpCode.NOT_FOUND,
            message=message,
            data={}
        )
    )

# 未授权的状态消息响应
def unauthorized_res(message: str = ""):
    return encode_json(
        Response(
            code = HttpCode.UNAUTHORIZED,
            message=message,
            data={}
        )
    )

# 无权限状态消息响应
def forbidden_res(message: str = ""):
    return encode_json(
        Response(
            code = HttpCode.FORBIDDEN,
            message=message,
            data={}
        )
    )