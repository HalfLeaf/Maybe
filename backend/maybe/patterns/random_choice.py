#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     随机数据生成获取
#
#  Author:      半片叶
#
#  Created:     2020.08.12
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

import numpy as np
from random import choice
from typing import Any,List,Dict


class randomChoice():
    def __init__(self, size:int=5):
        """
        随机选择类
        外部参数:
            :param size:生成的数据量总数
        """
        self.source = None
        self.data = None
        self.size = size
        self.choice_source = []
        self.weight = np.array([])

    def add(self, data:[List[Any], Dict]):
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

    def get(self, total:int=1) -> Any:
        """
        随机选择指定数量的样本
            :param total: 选择的数量
        :return:
        """
        try:
            total = int(total)
        except:
            total = 1
        p = self.weight if self.weight.size >0 else None
        if total<=1:
            return choice(list(np.random.choice(self.data, size=self.size, replace=True, p=p)))
        else:
            return list(np.random.choice(self.data, size=total, replace=True, p=p))

    def choice(self) -> Any:
        """
        获取一条随机选择的数据
        """
        if self.choice_source:
            return choice(self.data)
        elif self.weight.size > 0:
            self.choice_source = list(np.random.choice(self.data, size=self.size, replace=True, p=self.weight))
        else:
            self.choice_source = list(np.random.choice(self.data, size=self.size, replace=True))
        return choice(self.choice_source)
