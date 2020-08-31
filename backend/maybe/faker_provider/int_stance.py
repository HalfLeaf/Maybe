#-*-coding:utf-8-*-


'''
# ----------------------------------------------------------------------------
#  Purpose:     INT-Faker 实例对象
#
#  Author:      半片叶
#
#  Created:     2020.08.31
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

from faker import Faker
from faker.providers import BaseProvider

class IntStance(BaseProvider):
    def Int(self, **kwargs) -> int:
        """
         生成指定的整数类型测试数据
         外部参数:
                :param kwargs:是否必需参数
                :param equivalence_class_analysis:等价类划分法
                :param boundary_value_analysis:边界值分析法
                :param error_value_analysis:错误推测法
            内部参数:
                :private :
        """
        return 1

