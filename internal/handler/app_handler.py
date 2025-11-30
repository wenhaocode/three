# -*- coding: utf-8 -*-

"""
@Time   :2025/11/20 16:03
@Author : dongwenhao 
@File   : app_handler.py
"""
import os
from internal.schema.app_schema import CompletionForm, TestForm
# 引入langchain-openai工具类
from langchain_openai import ChatOpenAI
# 引入Response响应对象
from pkg.response import not_found_res, success_res
# 引入 自定义响应函数
from pkg.response import data_res, validate_error_res
# 引入AppService类
from internal.service.app_service import AppService
from internal.extension import db

# 定义控制器类
class AppHandler:
    """应用控制器"""

    def test_add_info(self):
        req_validate = TestForm()
        if not req_validate.validate():
            return validate_error_res(req_validate.errors)

        app_service = AppService(db)
        app_service.create_test(req_validate.data)

    def completion(self):
        # 实例化请求校验对象
        req_validate = CompletionForm()
        # 进行请求参数校验
        if not req_validate.validate():
            return validate_error_res(req_validate.errors)

        # 实例化一个langchain-openai对象
        llm = ChatOpenAI(
            model = "GPT-4o-2024-08-06",
            api_key=os.getenv("DEEPBRICKS_API_KEY"),
            base_url=os.getenv("DEEPBRICKS_BASE_URL"),
            temperature=os.getenv("MODEL_TEMPERATURE")
        )
        # 取得用户提问内容
        user_query = req_validate.data["user_query"]
        # 发起请求并得到结果
        res = llm.invoke(user_query)
        # 内容在响应体的content中
        data = res.content

        # 定义响应对象
        data = {"content": data}

        # 向前端返回数据
        return data_res(data, "大模型响应成功")

    # 定义一个测试接口
    def ping(self):
        return success_res("pong")
