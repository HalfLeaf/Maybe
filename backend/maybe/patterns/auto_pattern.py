#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     智能选值模式 · 数据生成获取
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


class AutoPattern():
    def __init__(self, algorithm:str=""):
        """
        智能选值模式数据生成类
        通过学习用户历次执行记录，智能生成符合用户期望的测试数据
        外部参数:
            :param algorithm: 数据学习算法，已支持如下算法:
                1.
        内部参数:

        备注:
            该类暂不开放，2.0版本之后开发
        """
        if algorithm in []:
            self.algorithm = algorithm
        else:
            self.algorithm = ""

    def get(self) -> Any:
        """
        获取数据集
        """
        pass
