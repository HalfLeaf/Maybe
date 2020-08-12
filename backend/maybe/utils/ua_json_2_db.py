#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     获取UserAgent每日流行数据
#
#  Author:      半片叶
#
#  Created:     2020.08.11
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''


from shadow_useragent import ShadowUserAgent


class userAgent():
    def __init__(self):
        """
        User-Agent 处理类
        外部参数:
            :param 无
        内部参数:
            :private user_agent: user_agent 代理选择列表
        """
        self.user_agent = []

    def get_user_agent(self):
        """
        根据用户代理json文件获取UserAgent
        """
        ua = ShadowUserAgent()
        ua.force_update()
        self.data = ua.get_uas()
        self.db.popular_user_agent.insert_many(self.data)
