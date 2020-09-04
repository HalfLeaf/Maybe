# -*-coding:utf-8-*-
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
from config import config
from maybe.utils import utils
from maybe.faker_provider import fake


class IntData():
    def __init__(self, **kwargs):
        """
        INT 整型数据对象
            外部参数:
                    :param kwargs:关键字参数
                        :param inter_bits:整数位数
                        :param max_value:整数范围最大值
                        :param min_value:整数范围最小值
                        :param exclude:排除选项
                        :param is_support_negative:是否支持负数
                        :param is_add_boundary_field:是否添加到边界域
            内部参数:
                    :private inter_bits:整数位数,可配置：
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
                    :private _inter_string_mapping: inter_bits参数为str时，映射关系表
        """
        self.inter_bits = kwargs.get('inter_bits', None)
        self.max_value = kwargs.get('max_value', None)
        self.min_value = kwargs.get('min_value', None)
        self.is_support_negative = kwargs.get('is_support_negative', False)
        self.exclude = kwargs.get('exclude', [])
        self.is_add_boundary_field = kwargs.get('is_add_boundary_field', True)

        self._inter_string_mapping = {
            "byte": 8,
            "short": 16,
            "int": 32,
            "long": 64,
        }
        self._exclude_flag = 1

    def parser(self):
        """
        解析数据
        """
        if self.inter_bits:
            self.max_value = None
            self.min_value = None
            self._parser_inter_bits()
        elif self.max_value is not None and self.min_value is not None:
            self.inter_bits = None
            self._parser_limit_values()
        else:
            self.inter_bits = config.DEFAULT_INTER_BIT

        self._parser_exclude_values()

    def get(self) -> int:
        """
        获取测试数据
        """
        value = fake.pyint(min_value=self.min_value, max_value=self.max_value)
        retry = 20
        while retry and self._exclude_flag and value in self.exclude:
            value = fake.pyint(min_value=self.min_value, max_value=self.max_value)
            retry = retry - 1
            if retry == 0:
                value = None
        while retry and not self._exclude_flag and self.exclude[0] <= value <= self.exclude[1]:
            value = fake.pyint(min_value=self.min_value, max_value=self.max_value)
            retry = retry - 1
            if retry == 0:
                value = None
        return value

    def _parser_inter_bits(self):
        """
        解析用户配置的整数位数
        """
        # 字符串形式进行整数转化
        if isinstance(self.inter_bits, str):
            self.inter_bits = self._inter_string_mapping.get(self.inter_bits.lower(), config.DEFAULT_INTER_BIT)

        if isinstance(self.inter_bits, int):
            try:
                self.inter_bits = int(self.inter_bits)
            except Exception as error:
                self.inter_bits = config.DEFAULT_INTER_BIT
                logging.error(f"inter_bits参数解析错误: {error}")
            self.max_value = 2 ** self.inter_bits
            self.min_value = -(2 ** self.inter_bits) if self.is_support_negative else 0
        else:
            logging.error(f"inter_bits用户配置类型错误")

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
        if abs(self.min_value) <= (2 ** 16 - 1):
            return 2 ** 16
        elif abs(self.min_value) <= (2 ** 32 - 1):
            return 2 ** 32
        elif abs(self.min_value) <= (2 ** 64 - 1):
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
            self.max_value = 2 ** config.DEFAULT_INTER_BIT
            return 0

        if abs(self.max_value) <= (2 ** 16):
            return 0
        elif abs(self.max_value) <= (2 ** 32):
            return 2 ** 16
        elif abs(self.max_value) <= (2 ** 64):
            return 2 ** 32
        else:
            logging.warning(f"用户设置的最大值超出位数限制！")
            return None

    def _generate_limit_value(self):
        """
        校验生成用户设置的最大值，最小值
        """
        try:
            self.max_value = int(self.max_value)
        except Exception as error:
            logging.error(f"用户设置的最大值转为数字失败:{error}")
            self.max_value = 2 ** config.DEFAULT_INTER_BIT

        try:
            self.min_value = int(self.min_value)
        except Exception as error:
            logging.error(f"用户设置的最小值转为数字失败:{error}")
            self.min_value = 0

        # 确保最大值大，最小值小
        if self.max_value < self.min_value:
            self.max_value, self.min_value = self.min_value, self.max_value

    def _parser_exclude_values(self):
        """
        解析需要从结果中排除的值
        """
        if isinstance(self.exclude, int):
            self.exclude = [self.exclude, ]
        elif isinstance(self.exclude, str):
            values = self.exclude.replace(" ", "").split("-")
            length = len(values)
            if length < 2:
                self.exclude = utils.str2int(values, [])
                return
            start = values[0]
            for i in range(length - 1, 0, -1):
                end = values[i]
                if end == start:
                    self.exclude = utils.str2int(start, [])
                    break
                elif start < end:
                    self._exclude_flag = 0
                    self.exclude = utils.str2int([start, end], [])
                    break
            else:
                self.exclude = utils.str2int(values, [])
