#-*-coding:utf-8-*-

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


def test_choice_pattern():
    from maybe.patterns.choice_pattern import ChoicePattern
    p = ChoicePattern()
    p.add({
        1:2,3:4, "df":"6", "sd":"s"
    }
    )
    for i in range(0, 20):
        a = p.get()
        print(a)


if __name__ == '__main__':
    test_choice_pattern()