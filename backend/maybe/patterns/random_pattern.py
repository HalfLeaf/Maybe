# -*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     随机模式 · 数据生成获取
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
from random import choice
from typing import Any, List, Dict


class RandomPattern():
    def __init__(self):
        """
        随机取值类
        外部参数:
            :param 无
        内部参数:
            :private data: 轮询数据源，目前只支持 List 和 Dict两种类型
        """
        self.data = None

    def add(self, data: [List[Any], Dict]):
        """
        添加数据集
            :param data: 数据集，目前只支持 List 和 Dict两种类型
            Dict类型只返回 Key 值，Value通过数据源自行取值
        """
        if isinstance(data, list):
            self.data = data
        elif isinstance(self.data, dict):
            self.data = list(data.keys())
        else:
            self.data = [data]

    def get(self) -> Any:
        """
        遍历数据集，获取一个可用的数据
        返回值:
            任意类型的数据单元
        """
        return choice(self.data)
