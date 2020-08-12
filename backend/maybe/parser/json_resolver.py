#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#    Purpose:     json对象解析器
#
#    Author:      半片叶
#
#    Created:     2020.06.10
#
#    ██╗   ██╗  ███████╗
#    ╚██╗ ██╔╝  ██╔════╝
#     ╚████╔╝   █████╗
#      ╚██╔╝    ██╔══╝
#       ██║     ███████╗
#       ╚═╝     ╚══════╝
# ----------------------------------------------------------------------------
'''


import logging

from maybe.parser.prepare_data import dataHandler
from maybe.parser.prepare_request import requestInstance
from maybe.parser.prepare_response import responseInstance


logger = logging.getLogger(__name__)


class jsonResolver():
    def __init__(self, data:dict):
        """
        json内容解析器
            外部参数:
                :param data: json文件内容，字典形式
            内部参数:
                :private cook: 数据验证处理器
                :private _url:请求地址，必需参数
                :private _name:用例名称
                :private _id:用例id
                :private _description:用例描述
                :private _parent_name:父级名称
                :private _parent_id:父级id
                :private _test_total:测试总数
                :private _method:请求方式
                :private _concurrent:并发数
                :private _request:请求对象
                :private _response:响应对象
        """
        self.data = data
        self.cook = dataHandler()
        self._url = ""
        self._name = ""
        self._id = ""
        self._description = ""
        self._parent_name = ""
        self._parent_id = ""
        self._test_total = 1
        self._concurrent = 1
        self._method = "GET"
        self._request = {}
        self._response = {}

    @property
    def name(self) -> str:
        return self._name

    def parser(self):
        """
        解析主程序
        """
        self._url = self.data.get("url", "")
        if not self._url:
            return
        self._name = self.cook.cook_name(self.data.get("name", ""), self._url)
        self._id = self.cook.cook_case_id(self.data.get("id", 0))
        self._description = self.data.get("description", "")

        self._parent_id = self.cook.cook_parent_id(self.data.get("parent_id", 0))
        if not self._parent_id:
            self._parent_name = self.cook.cook_parent_name(self.data.get("parent_name", ""))

        self._test_total = self.cook.cook_test_total(self.data.get("test_total", 10))
        self._concurrent = self.cook.cook_concurrent(self.data.get("concurrent", 1))

        self._method = self.cook.cook_method(self.data.get("method", "GET"))
        self._request = requestInstance(self.data.get('request', {}))
        self._response = responseInstance(self.data.get('response', {}))


