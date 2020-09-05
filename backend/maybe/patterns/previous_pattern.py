# -*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     恢复前次模式 · 数据生成获取
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

from typing import Any,List,Dict


class PreviousPattern():
    def __init__(self):
        """
        轮询遍历类
        外部参数:
            :param 无
        内部参数:
            :private data: 轮询数据源，目前只支持 List 和 Dict两种类型
            :private _total: 数据源条目总数
            :private _circle_index: 当前轮询索引下标值
        """
        self.data = None
        self._total = 0
        self._circle_index = -1

    def add(self, data:[List[Any], Dict]):
        """
        添加数据集
            :param data: 数据集，目前只支持 List 和 Dict两种类型
            Dict类型只返回 Key 值，Value通过数据源自行取值
        """
        if isinstance(data, list):
            self.data = data
        elif isinstance(self.data, dict):
            self.data = list(data.keys())
        self._total = len(self.data)

    def get(self) -> Any:
        """
        遍历数据集，获取一个可用的数据
        返回值:
            任意类型的数据单元
        """
        if not self._total:
            return None
        self._circle_index = self._circle_index + 1
        if self._circle_index + 1 > self._total:
            self._circle_index = 0
        return self.data[self._circle_index]
