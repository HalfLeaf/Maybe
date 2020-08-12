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

import numpy as np
from random import choice
from typing import Generator,Any


class randomChoice():
    def __init__(self):
        """
        随机选择类
        """
        self.source = None
        self.data = None
        self.choice_source = []
        self.weight = np.array([])

    def add(self, data:[list, dict]):
        """
        添加数据集
            :param data: 数据集
        :return:
        """
        self.source = data
        self.data = data
        self._handle_data_source()

    def _handle_data_source(self):
        """
        处理数据源
        """
        if isinstance(self.source, list):
            self.data = self.source
            self.weight = np.array([])
        elif isinstance(self.source, dict):
            self.data = list(self.source.keys())
            _weight = np.array(list(self.source.values()))
            self.weight = _weight / _weight.sum() if _weight.sum() != 0 else None

    def get(self, total:int=1) -> Generator:
        """
        随机选择指定数量的样本
            :param total: 选择的数量
        :return:
        """
        if self.weight.size > 0:
            yield from list(np.random.choice(self.data, size=total, replace=True, p=self.weight))
        else:
            yield from list(np.random.choice(self.data, size=total, replace=True))

    def choice(self) -> Any:
        """
        获取一条随机选择的数据
        """
        if self.choice_source:
            return choice(self.data)
        elif self.weight.size > 0:
            self.choice_source = list(np.random.choice(self.data, size=20, replace=True, p=self.weight))
        else:
            self.choice_source = list(np.random.choice(self.data, size=20, replace=True))
        return choice(self.choice_source)
