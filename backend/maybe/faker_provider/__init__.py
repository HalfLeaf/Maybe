#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     自定义生成的Faker对象
#
#  Author:      半片叶
#
#  Created:     2020.08.31
#
#        _        __    _     ___   ____
#       | |\/|   / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

from faker import Faker

class FakerInstance():
    def __init__(self, is_new: bool = True, locales: str = "zh_CN"):
        """
        全局实例化Faker对象
            外部参数:
                无
            内部参数:
                :private fake: Faker实例对象
        """
        if is_new:
            Faker.seed(0)
        self._fake = Faker(locales)
        # self.faker.add_provider()

    @property
    def fake(self):
        return self._fake


fake = FakerInstance().fake
