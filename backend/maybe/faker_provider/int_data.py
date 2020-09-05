# -*-coding:utf-8-*-


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
                    :param kwargs:关键字参数
                        :param max_value:整数范围最大值
                        :param min_value:整数范围最小值
                        :param is_support_negative:是否支持负数
            内部参数:
                    :private
        """
        max_value = kwargs.get('max_value', None)
        min_value = kwargs.get('min_value', None)
        is_support_negative = kwargs.get('is_support_negative', False)




