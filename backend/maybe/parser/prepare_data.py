#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#    Purpose:     数据预处理器
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
from pathlib import Path
from typing import Dict, List, Sequence

from maybe.instance.user_agent import userAgent
from maybe.instance.int_instance import IntData
from maybe.instance.list_instance import ListData
from maybe.instance.bool_instance import BoolData
from maybe.instance.dict_instance import DictData
from maybe.instance.float_instance import FloatData
from maybe.instance.string_instance import StringData

logger = logging.getLogger(__name__)

class dataHandler():
    # 数据验证处理器
    def cook_name(self, name:str, url:str) -> str:
        """
        验证用例名称
            :param name: 用户输入的名称
            :param url: 用户输入的url地址
        :return:
        """
        name = name if name else url
        return name

    def cook_test_total(self, test_total:int) -> int:
        """
        验证用例测试次数
            :param test_total: 测试次数
        :return:
        """
        try:
            test_total = int(test_total)
        except Exception as error:
            logger.error(f"验证用例测试次数错误：{error}")
            test_total = 10
        test_total = test_total if test_total > 0 else 1
        return test_total

    def cook_concurrent(self, concurrent:int) -> int:
        """
        验证用例并发次数
            :param concurrent: 并发次数
        :return:
        """
        try:
            concurrent = int(concurrent)
        except Exception as error:
            logger.error(f"验证用例并发次数错误：{error}")
            concurrent = 1
        concurrent = concurrent if concurrent > 0 else 1
        return concurrent

    def cook_method(self, method:str) -> str:
        """
        验证用例请求方式
            :param method: 请求方式
        :return:
        """
        try:
            method = str(method).upper()
        except Exception as error:
            logger.error(f"验证用例请求方式错误：{error}")
            method = "GET"
        method = method if method in ["GET", "POST", "PUT", "DELETE"] else "GET"
        return method

    def cook_case_id(self, case_id:int) -> int:
        """
        验证用例id
            :param case_id: 用例id
        :return:
        """
        try:
            case_id = int(case_id)
        except Exception as error:
            logger.error(f"验证用例id错误：{error}")
            case_id = 0
        # TODO 添加到数据库，并保证全局唯一
        return case_id

    def cook_parent_id(self, parent_id:int) -> int:
        """
        验证用例父级id
            :param parent_id: 用例父级id
        :return:
        """
        try:
            parent_id = int(parent_id)
        except Exception as error:
            logger.error(f"验证用例父级id错误：{error}")
            parent_id = 0
        # TODO 数据库验证是否真的存在
        return parent_id

    def cook_parent_name(self, parent_name:str) -> int:
        """
        验证用例id
            :param case_id: 用例id
        :return:
        """
        # TODO 数据库验证是否真的存在，并转换为数据库索引值
        return 0

    def cook_cookies(self, cookies:[Dict, str]) -> [Dict, str]:
        """
        处理请求对象的cookies
        :return:
        """
        cookies = cookies if cookies else None
        return cookies

    def cook_auth(self, auth:[Dict, str]) -> [Dict, str]:
        """
        处理请求对象的auth
        :return:
        """
        auth = auth if auth else None
        return auth

    def cook_files(self, files:list) -> List[str]:
        """
        处理请求对象的files
        :return:
        """
        multiple_files = []
        if isinstance(files, list):
            # windows打开的文件数有512个限制
            for file in files[:512]:
                path = Path(file)
                if path.exists() and path.is_file():
                    multiple_files.append(path.name)
        multiple_files = multiple_files if multiple_files else None
        return multiple_files

    def cook_user_agent(self, user_agent:[str, Dict]) -> userAgent:
        """
        处理用户代理
        """
        UA = userAgent()
        if isinstance(user_agent, str):
            UA.set(user_agent)
        elif isinstance(user_agent, dict):
            type = user_agent.get('type', "String").lower()
            if type == "string":
                UA.set(user_agent.get('value', ""))
            elif type == "dict":
                content = user_agent.get('value', {})
                pattern = content.get('pattern', "default").lower()
                if pattern == "random":
                    UA.get_random_user_agent()
                elif pattern == "choice":
                    dataset = self.cook_dataset(content.get('dataset', []))
                    UA.set_choice_type("choice")
                    UA.add(dataset)
                elif pattern == "circle":
                    dataset = self.cook_dataset(content.get('dataset', []))
                    UA.set_choice_type("circle")
                    UA.set(dataset)
                else:
                    UA.get_random_user_agent()
        return UA

    def cook_headers(self, headers:Dict) -> [Dict, userAgent]:
        """
        处理请求对象的headers
        """
        user_agent = {}
        if isinstance(headers, dict):
            user_agent = headers.pop('user_agent', "")
        else:
            headers = {}
        ua = self.cook_user_agent(user_agent)
        return headers, ua

    def cook_dataset(self, dataset:List) -> Dict:
        """
        处理用户数据集
        """
        tmp = {}
        if isinstance(dataset, list):
            for data in dataset:
                if isinstance(data, dict):
                    key = data.get('value', "")
                    value = data.get('weight', 1)
                    if key and not key in [0, ""]:
                        tmp[key] = value
                elif isinstance(data, str):
                    tmp[data] = ""
            min_value = self.compute_min_value(tmp.values())
            for key, value in tmp.items():
                try:
                    tmp[key] = value
                except:
                    tmp[key] = min_value

        elif isinstance(dataset, dict):
            min_value = self.compute_min_value(dataset.values())
            for key, value in dataset.items():
                try:
                    tmp[key] = value
                except:
                    tmp[key] = min_value
        return tmp

    def compute_min_value(self, numbers:Sequence) -> int:
        """
        计算列表序列中的最小值
            :param number: 序列
        :return: 序列中的最小值
        """
        number = []
        for v in numbers:
            try:
                number.append(int(v))
            except:
                pass
        if number:
            min_value = min(number)
        else:
            min_value = 1
        return min_value

    def cook_params(self, params:List) -> Dict:
        """
        处理请求对象的params
            :param params: 请求对象的params
        :return:
        """
        data = {}
        if isinstance(params, list):
            for param in params:
                type = param.get('type', "string").lower()
                name = param.get('name', "")
                obj = None
                require = param.get('require', True),
                equivalence_class_analysis = param.get('Equivalence-Class-Analysis', {})
                boundary_value_analysis = param.get('Boundary-Value-Analysis', {})
                error_value_analysis = param.get('Error-Value-Analysis', {})
                if type == "int":
                    obj = IntData(require,
                                  equivalence_class_analysis,
                                  boundary_value_analysis,
                                  error_value_analysis)
                elif type == "float":
                    obj = FloatData()
                elif type == "string":
                    obj = StringData()
                elif type == "list":
                    obj = ListData()
                elif type == "dict":
                    obj = DictData()
                elif type == "bool":
                    obj = BoolData()
                data.update({name: obj})
        elif isinstance(params, dict):
            pass
        else:
            return data

