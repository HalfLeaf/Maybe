#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     UserAgent实例对象
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
import fake_useragent
from shadow_useragent import ShadowUserAgent

from models import MongoDatabase
from maybe.patterns.random_choice import randomChoice
from maybe.patterns.circle_pattern import CirclePattern

USER_AGENT_PATTERN = ["random", "circle", "choice", "popular", "default"]
DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"

class popularUserAgent():
    def __init__(self):
        """
        popularUserAgent 获取流行的UserAgent
        外部参数:
            :param 无
        内部参数:
            :private user_agent: user_agent列表
            :private db: 数据库操作对象
        """
        self.user_agent = []

    def set(self):
        """
        通过 ShadowUserAgent 库获取流行的UserAgent
        并存入到数据库 popular_user_agent 集合中
        """
        try:
            ua = ShadowUserAgent()
            ua.force_update()
            self.data = ua.get_uas()
            self.db = MongoDatabase().db
            # 清空现有数据
            self.db.popular_user_agent.drop()
            self.db.popular_user_agent.insert_many(self.data)
        except Exception as error:
            logging.error(f"设置流行UserAgent列表信息错误：{error}")

    def get(self):
        """
        通过数据库获取所有 popular_user_agent
        并生成随机对象
        """
        if not self.user_agent:
            try:
                self.db = MongoDatabase().db
                cursor = self.db.popular_user_agent.find()
                self.user_agent = [x.get('useragent', DEFAULT_USER_AGENT) for x in cursor if x.get('useragent', "")]
            except Exception as error:
                logging.error(f"获取流行UserAgent列表信息错误：{error}")
            self.random = randomChoice()
            self.random.add(self.user_agent)
        return self.random.get()


class userAgent():
    def __init__(self):
        """
        User-Agent 处理类
        外部参数:
            :param 无
        内部参数:
            :private user_agent: user_agent 代理选择列表
            :private choice_type: 用户选择的方式
        """
        self.user_agent = []
        self.choice_type = "Default"

    def set_choice_type(self, choice_type:str):
        """
        设置用户选择方式
            :param choice_type: 用户选择方式
        """
        if choice_type.lower() in USER_AGENT_PATTERN:
            self.choice_type = choice_type.lower().title()
        else:
            self.choice_type = "Default"



