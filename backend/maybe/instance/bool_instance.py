#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     BOOL类型实例对象
#
#  Author:      半片叶
#
#  Created:     2020.08.11
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

from typing import Any
from maybe.patterns.random_pattern import RandomPattern

class BoolData():
    def __init__(self):
        """
        Bool类型测试数据
            外部参数:
                无
            内部参数:
                :private _random:随机取值对象
        """
        self._random = RandomPattern()

    def get(self, field="") -> Any:
        """
        获取bool类型值
            外部参数:
                :param field:指定的参数域
            返回值:
        """
        pass

    def _get_effective_field(self) -> bool:
        """
        获取Bool类型的有效域
            外部参数:
                无
            返回值:
                正确的Python Bool类型数据
        """
        return self._random.get()

    def _get_invalid_field(self) -> bool:
        """
        获取Bool类型的无效域
            外部参数:
                无
            返回值:
                正确的Python Bool类型数据
        """
        return self._random.get()

