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


def test_popular_user_agent():
    from maybe.instance.user_agent import popularUserAgent
    p = popularUserAgent()
    for i in range(0, 20):
        a = p.get()
        assert isinstance(a, str)


if __name__ == '__main__':
    test_popular_user_agent()