# -*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     
#
#  Author:      半片叶
#
#  Created:     2020.09.04
#
# ----------------------------------------------------------------------------
'''

from typing import List


def str2int(value: [str, List[str]], container: List[int]) -> List[int]:
    """
    字符串转整数
        外部参数：
            :param value: 整数值
            :param container: 存储容器
    """
    try:
        if isinstance(value, str):
            container.append(int(value))
        elif isinstance(value, list):
            for x in value:
                try:
                    container.append(int(x))
                except Exception as error:
                    pass
    except Exception as error:
        pass

    return container
