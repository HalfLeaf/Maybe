# -*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     FLOAT 实例对象
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
from maybe.faker_provider import fake

class FloatData():
    def __init__(self, **kwargs):
        """
        INT 整型数据对象
            外部参数:
                    :param kwargs:关键字参数
                        :param inter_bits:整数位数
                        :param decimal_bits:小数部分位数
                        :param max_value:整数范围最大值
                        :param min_value:整数范围最小值
                        :param is_support_negative:是否支持负数
            内部参数:
                    :private inter_bits:整数位数
                    :private decimal_bits:小数部分位数
                    :private max_value:整数范围最大值
                    :private min_value:整数范围最小值
                    :private is_support_negative:是否支持负数
        """
        self.max_value = kwargs.get('max_value', None)
        self.min_value = kwargs.get('min_value', None)
        self.inter_bits = kwargs.get('inter_bits', None)
        self.is_support_negative = kwargs.get('is_support_negative', False)
        self.decimal_bits = kwargs.get('decimal_bits', config.DEFAULT_FLOAT_DECIMAL_BIT)

    def parser(self):
        """
        解析生成浮点数对象
        """
        if self.inter_bits:
            self.max_value = None
            self.min_value = None
            self._parser_inter_bits()
        elif self.max_value is not None and self.min_value is not None:
            self.inter_bits = None
            self._parser_limit_values()
        else:
            self.inter_bits = config.DEFAULT_FLOAT_DECIMAL_BIT

        self.is_support_negative = False if self.is_support_negative else True
        try:
            self.decimal_bits = int(self.decimal_bits)
        except Exception as error:
            logging.error(f"用户配置小数位数错误：{error}")
            self.decimal_bits = config.DEFAULT_FLOAT_DECIMAL_BIT

    def _parser_inter_bits(self):
        """
        解析用户配置的整数位数
        """
        # 字符串形式进行整数转化
        if isinstance(self.inter_bits, int):
            try:
                self.inter_bits = int(self.inter_bits)
            except Exception as error:
                self.inter_bits = config.DEFAULT_FLOAT_INTER_BIT
                logging.error(f"inter_bits参数解析错误: {error}")
        else:
            logging.error(f"inter_bits用户配置类型错误")
            self.inter_bits = config.DEFAULT_FLOAT_INTER_BIT

    def _parser_limit_values(self):
        """
        解析用户配置的范围限定值参数
        """
        if self.max_value is not None:
            try:
                self.max_value = int(self.max_value)
            except Exception as error:
                logging.error(f"用户配置的范围最大值错误: {error}")
                self.max_value = None

        if self.min_value is not None:
            try:
                self.min_value = int(self.min_value)
            except Exception as error:
                logging.error(f"用户配置的范围最小值错误: {error}")
                self.min_value = None

    def get(self):
        """
        获取测试数据
        """
        value = fake.pyfloat(left_digits=self.inter_bits,
                             right_digits=self.decimal_bits,
                             positive=self.is_support_negative,
                             min_value=self.min_value,
                             max_value=self.max_value)
        # 预留处理小数点右侧部分位数不足的情况
        v = str(value).split(".")
        try:
            inter = v[0]
            decimal = v[1]
        except:
            inter = 1
            decimal = "1" * self.decimal_bits
        length = len(inter)
        if length < self.inter_bits:
            inter = f"{inter}{'0'*(self.inter_bits - length)}"
        elif length > self.inter_bits:
            inter = inter[:self.inter_bits]
        return float(f"{inter}.{decimal}")
