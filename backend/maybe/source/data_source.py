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

import pathlib
from typing import List

class dataSource():
    def __init__(self, target_path:str="."):
        """
        类初始化
            外部参数:
                :param target_path: 存储用户测试数据的目标路径，默认当前目录
            内部参数:
                :private _json_files:目标路径下所有的json文件
                :private _xml_files:目标路径下所有的xml文件
        """
        self.target_path = target_path
        self._json_files = []
        self._xml_files = []

    def get_files(self):
        """
        解析目标路径，获取所有指定后缀的文件路径
            目标路径为空目录时：触发 FileNotFoundError
            目标路径为非目录且文件后缀名不是json或者xml：触发 ValueError
            目标路径不存在时：触发 FileExistsError
        """
        path = pathlib.Path(self.target_path)
        if path.exists():
            if path.is_dir():
                self._json_files = [x for x in path.glob('*.json')]
                self._xml_files = [x for x in path.glob('*.xml')]
                if not (self._xml_files or self._json_files):
                    raise FileNotFoundError(f"{self.target_path} 目录下无法找到可用的json或者xml文件！")
            elif path.suffix == '.json':
                self._json_files.append(self.target_path)
            elif path.suffix == '.xml':
                self._xml_files.append(self.target_path)
            else:
                raise ValueError(f"{self.target_path} 路径不存在，无法获取到测试数据！")
        else:
            raise FileExistsError(f"{self.target_path} 路径不存在，无法获取到测试数据！")

    @property
    def json_files(self) -> List[str]:
        """
        获取目标路径下所有的json文件
            :return json文件路径列表
        """
        return self._json_files

    @property
    def xml_files(self) -> List[str]:
        """
        获取目标路径下所有的xml文件
            :return xml文件路径列表
        """
        return self._xml_files
