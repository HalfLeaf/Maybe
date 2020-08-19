#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     挑选模式 · 数据生成获取
#
#  Author:      半片叶
#
#  Created:     2020.08.14
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

import numpy as np
from random import choice
from typing import Any,List,Dict


class ChoicePattern():
    def __init__(self, size: int = 5):
        """
        随机选择类
        外部参数:
            :param size:生成的数据量总数
        内部参数:
            :private data:数据源
            :private weight:权重配置
        """
        self.data = None
        self.size = size
        self.weight = np.array([])

    def add(self, data: [List[Any], Dict]):
        """
        添加数据集
            :param data: 数据集，支持列表和字典
                列表：列表中的每一单元都是一条数据

                字典：key值为测试数据，value配置对应的权重
        :return:
        """
        if isinstance(data, list):
            flag = False
            values = []
            weights = []
            for x in data:
                if isinstance(x, dict):
                    value = x.get('value', "")
                    weight = x.get('weight', 0)
                    if value and weight:
                        flag = True
                    value = value if value else x
                    values.append(value)
                    weight = weight if weight else 10
                    weights.append(weight)
                else:
                    values.append(x)
                    if flag:
                        weights.append(10)
            self.data = values
            self.weight = np.array([x/sum(weights) for x in weights]) if flag else np.array([])
        elif isinstance(data, dict):
            self.data = list(data.keys())
            weights = []
            for x in list(data.values()):
                try:
                    x = int(x)
                except:
                    x = 10
                weights.append(x)
            _weight = np.array(weights)
            self.weight = _weight / _weight.sum() if _weight.sum() != 0 else None

    def get(self, total: int = 1) -> Any:
        """
        随机选择指定数量的样本
            :param total: 选择的数量
        :return:
        """
        try:
            total = int(total)
        except:
            total = 1
        p = self.weight if self.weight.size > 0 else None
        if total <= 1:
            return choice(list(np.random.choice(self.data, size=self.size, replace=True, p=p)))
        else:
            return list(np.random.choice(self.data, size=total, replace=True, p=p))
