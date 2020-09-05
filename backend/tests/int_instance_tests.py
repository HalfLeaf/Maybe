# -*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     UserAgent类调试文件
#
#  Author:      半片叶
#
#  Created:     2020.08.13
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''


def test_int_instance():
    from maybe.instance.int_instance import IntData
    p = IntData(inter_bits=8, is_support_negative=True, exclude="1 - 89 ")
    p.parser()
    for i in range(0, 20):
        a = p.get()
        print(a)


if __name__ == '__main__':
    test_int_instance()