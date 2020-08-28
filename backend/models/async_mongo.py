#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     异步连接MongoDB数据库
#
#  Author:      半片叶
#
#  Created:     2020.08.28
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

import asyncio
from urllib import parse
from motor.motor_asyncio import AsyncIOMotorClient

from config import config


class Motor_Connection():
    __instance = None
    def __new__(cls):
        if Motor_Connection.__instance is None:
            Motor_Connection.__instance = object.__new__(cls)
            try:
                loop = asyncio.get_event_loop()
            except:
                loop = asyncio.new_event_loop()

            Motor_Connection.__instance.client = AsyncIOMotorClient(
                f"mongodb://{parse.quote_plus(config.MONGODB_USERNAME)}:{parse.quote_plus(config.MONGODB_PASSWORD)}@{config.MONGODB_IP}:{config.MONGODB_PORT}",
                io_loop=loop
            )
            Motor_Connection.__instance =  Motor_Connection.__instance.client
        return Motor_Connection.__instance

    def __init__(self, db_name="maybe"):
        """
        实例化数据库对象，连接
        外部参数:
            :param db_name: 连接的数据库名称，默认为maybe
        内部参数:
            db:数据库操作对象
        """
        self._db = Motor_Connection.__instance[db_name]

    @property
    def db(self):
        """获取数据库操作对象"""
        return self._db
