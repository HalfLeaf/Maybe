#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     默认值模式 · 数据生成获取
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


class DefaultPattern():
    def __init__(self, ins:str=""):
        """
        默认值模式 · 数据生成类
        通过获取 数据库中已保存的每种实例对象的默认值信息
        返回给用户当前实例对象的默认值
        外部参数:
            :param ins: 数据对象类型
                1.
        内部参数:
        """

        if ins.lower() in []:
            self.ins = ins
        else:
            self.ins = ""

    def get(self) -> Any:
        """
        获取数据集
        """
        pass