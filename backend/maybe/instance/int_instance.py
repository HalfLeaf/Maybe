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
import logging
from typing import List, Dict


class IntData():
    def __init__(self, **kwargs):
        """
        INT 整型数据对象
            外部参数:
                    :param kwargs:关键字参数
                        :param interer_bits:整数位数
                        :param max_value:整数范围最大值
                        :param min_value:整数范围最小值
                        :param exclude:排除选项
                        :param is_support_negative:是否支持负数
                        :param is_add_boundary_field:是否添加到边界域
            内部参数:
                    :private interer_bits:整数位数,可配置：
                        参数类型: int/string
                        可支持配置:
                            8 / byte
                            16 / short
                            32 / int
                            64 / long
                    :private max_value:整数范围最大值
                    :private min_value:整数范围最小值
                    :private exclude:排除选项
                    :private is_support_negative:是否支持负数
                    :private is_add_boundary_field:是否添加到边界域
        """
        self.interer_bits = kwargs.get('interer_bits', None)
        self.max_value = kwargs.get('max_value', None)
        self.min_value = kwargs.get('min_value', None)
        self.is_support_negative = kwargs.get('is_support_negative', False)
        self.exclude = kwargs.get('exclude', [])
        self.is_add_boundary_field = kwargs.get('is_add_boundary_field', True)

    def parser(self):
        """
        解析数据
        """
        if self.interer_bits:
            self.max_value = None
            self.min_value = None
        elif not self.max_value is None and not self.min_value is None:
            self.interer_bits = None
            self._parser_limit_values()
        else:
            self.interer_bits = 32

    def get(self) ->int:
        """
        获取测试数据
        """
        pass

    def _parser_interer_bits(self):
        pass

    def _parser_limit_values(self):
        """
        解析用户配置的范围限定值参数
        """
        if self.max_value is None:
            self.max_value = self._generate_max_value()
        elif self.min_value is None:
            self.max_value = self._generate_min_value()
        else:
            self._generate_limit_value()

    def _generate_max_value(self) -> [int, None]:
        """
        根据用户设置的最小值，生成对应的最大值
            返回值:
                :return: 生成的对应最大范围值
        """
        try:
            self.min_value = int(self.min_value)
        except Exception as error:
            logging.error(f"根据用户设置的最小值，生成对应的最大值错误:{error}")
            self.min_value = 0
            return 2 ** 16
        if abs(self.min_value) <= (2**16 -1):
            return 2 ** 16
        elif abs(self.min_value) <= (2**32 -1):
            return 2 ** 32
        elif abs(self.min_value) <= (2**64 -1):
            return 2 ** 64
        else:
            logging.warning(f"用户设置的最小值超出位数限制！")
            return None

    def _generate_min_value(self) -> [int, None]:
        """
        根据用户设置的最大值，生成对应的最小值
            返回值:
                :return: 生成的对应最小范围值
        """
        try:
            self.max_value = int(self.max_value)
        except Exception as error:
            logging.error(f"根据用户设置的最小值，生成对应的最大值错误:{error}")
            self.max_value = 2 ** 16
            return 0

        if abs(self.max_value) <= (2**16):
            return 0
        elif abs(self.max_value) <= (2**32):
            return 2 ** 16
        elif abs(self.max_value) <= (2**64):
            return 2 ** 32
        else:
            logging.warning(f"用户设置的最大值超出位数限制！")
            return None

    def _generate_limit_value(self):
        """
        校验生成用户设置的最大值，最小值
        """
        pass


