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
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

from faker import Faker
from maybe.faker_provider.int_stance import IntStance


class FakerInstance():
    def __init__(self):
        """
        全局实例化Faker对象
            外部参数:
                无
            内部参数:
                :private faker: Faker实例对象
        """
        self.faker = Faker()
        self.faker.add_provider(IntStance)

    @property
    def faker(self):
        return self.faker


faker = FakerInstance().faker
