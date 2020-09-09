# -*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     BOOL类型实例对象
#
#  Author:      半片叶
#
#  Created:     2020.08.11
#
#         _       __    _     ___   ____
#        | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

from maybe.faker_provider import fake

class BoolData():
    def __init__(self):
        """
        Bool类型测试数据
            外部参数:
                无
            内部参数:
                无
        """
        pass

    def parser(self):
        pass

    def get(self) -> bool:
        return fake.pybool()