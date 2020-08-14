#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     INT 实例对象
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

from typing import List, Dict


class IntData():
    def __init__(self, require:bool, equivalence_class_analysis:Dict,
                 boundary_value_analysis:Dict, error_value_analysis:Dict):
        """
        INT 整型数据对象
            外部参数:
                :param require:是否必需参数
                :param equivalence_class_analysis:等价类划分法
                :param boundary_value_analysis:边界值分析法
                :param error_value_analysis:错误推测法
            内部参数:

        """
        self.require = require
        self.error_value_analysis = error_value_analysis
        self.boundary_value_analysis = boundary_value_analysis
        self.equivalence_class_analysis = equivalence_class_analysis

    def parser(self):
        """
        解析数据
        """
        pass


    def get(self) ->int:
        """
        获取测试数据
        """
        pass

