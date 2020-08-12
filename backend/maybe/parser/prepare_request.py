#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#    Purpose:     用于获取数据源文件
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

from typing import List, Dict
from maybe.parser.prepare_data import dataHandler


class requestInstance():
    def __init__(self, request:dict):
        """
        request对象解析类
            外部参数:
                :param request: 用户定义的request请求内容
            内部参数:
                :private cook: 数据验证处理器
                :private _cookies:cookies信息
                :private _auth:auth认证信息
                :private _files:files传输文件列表
                :private _headers:请求头headers信息
                :private _user_agent:请求头headers中user_agent信息
        """
        self.request = request
        self.cook = dataHandler()
        self._cookies = None
        self._auth = None
        self._files = None
        self._headers = None
        self._user_agent = None
        self._params = None
        self._data = None

    def _check_source(self) -> bool:
        """
        检查数据源是否合法
        """
        if isinstance(self.request, dict):
            return True
        else:
            return False

    def parser(self):
        """
        解析处理request对象
        """
        if self._check_source():
            self._cookies = self.cook.cook_cookies(self.request.get("cookies", ""))
            self._auth = self.cook.cook_auth(self.request.get("auth", {}))
            self._files = self.cook.cook_files(self.request.get("files", []))
            self._headers, self._user_agent = self.cook.cook_headers(self.request.get("headers", {}))
            self._params = self.cook.cook_params(self.request.get("params", []))
            self._data = self.cook.cook_params(self.request.get("data", []))

    @property
    def cookies(self) -> [Dict, str]:
        """
        获取请求对象的cookies
        """
        return self._cookies

    @property
    def auth(self) -> [Dict, str]:
        """
        获取请求对象的auth
        """
        return self._auth

    @property
    def files(self) -> List[str]:
        """
        获取请求对象的files
        """
        return self._files

    @property
    def headers(self):
        """
        获取请求对象的headers
        """
        self._headers.update(self._user_agent.get())
        return self._headers

    @property
    def params(self) -> Dict:
        """
        处理请求参数信息
        """
        return self._params

    @property
    def data(self) -> Dict:
        """
        处理请求参数信息
        """
        return self._data
