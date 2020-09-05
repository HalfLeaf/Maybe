# -*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     同步连接MongoDB数据库对象
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

from pymongo import MongoClient

from config import config

class MongoDatabase():
    """
    创建MongoDB数据库操作对象，默认单实例模式
        可通过关键字参数设置是否创建新的连接对象:
            :param new_instance 来控制是否创建新实例对象
            :param db_name 连接的数据库名称
                默认值: maybe
        内部参数:
            :private _db:数据库操作对象
    """
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance or kw.get("new_instance", False):
            cls._instance = super(MongoDatabase, cls).__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self, db_name="maybe"):
        """
        实例化数据库对象，连接
        外部参数:
            :param db_name: 连接的数据库名称，默认为maybe
        内部参数:
            db:数据库操作对象
        """
        client = MongoClient(host=config.MONGODB_IP, port=config.MONGODB_PORT)
        self._db = client[db_name]
        self._db.authenticate(config.MONGODB_USERNAME, config.MONGODB_PASSWORD)

    @property
    def db(self) -> MongoClient:
        """获取数据库操作对象"""
        return self._db
